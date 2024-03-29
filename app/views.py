from pathlib import Path

from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone

from app.forms import ImageFileForm, ContactForm
from app.models import ImageFileModel
from dog_cat_judgement.settings import MEDIA_ROOT, MAX_SIZE_UPLOAD

from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def index(request):
    """
    ビュー : ホームページ
        POSTリクエストの場合
            画像をサーバーにアップロードし、判別処理を行う
            処理結果に応じて情報を設定し、HttpResponseを返却する
        GETリクエストの場合
            ホームページを表示する

    Parameters
    ----------
    request : HttpRequest
        ページに対するリクエスト

    Returns
    -------
    HttpResponse
        処理結果に応じたレスポンス

    """
    if request.method == 'POST':
        form = ImageFileForm(request.POST or None, request.FILES)
        if form.is_valid():
            if request.FILES['image'].size > MAX_SIZE_UPLOAD:
                logger.debug("[failure] over file size")
                messages.warning(request, 'アップロード可能な画像ファイルの最大サイズは1MBです')
                return render(request, 'app/index.html', {'form': form})

            image_file = ImageFileModel()
            image_file.image = request.FILES['image']
            image_file.published_date = timezone.now()

            image_file.save()
            form.save()

            from app.judgement import judgement
            path = Path(MEDIA_ROOT) / image_file.image.name
            try:
                logger.debug("[start] judge dogs vs cats")
                result = judgement(path)
                logger.debug("[end] judge dogs vs cats")
                if result < 0.5:
                    context = {'result': round(100 - result * 100, 1), 'animal': '犬', 'image': image_file.image.name}
                else:
                    context = {'result': round(result * 100, 1), 'animal': '猫', 'image': image_file.image.name}
            except Exception as e:
                logger.debug("[exception] judgement error" + e.__class__.__name__)
                messages.error(request, '判定に失敗しました。')
                return render(request, 'app/index.html', {'form': form})

            return render(request, 'app/result.html', context)
        else:
            form = ImageFileForm()
            logger.debug("[failure] form valid")
            messages.warning(request, '画像ファイル(jpg, png, gif)を選択して下さい。')
            return render(request, 'app/index.html', {'form': form})
    else:
        form = ImageFileForm()
        return render(request, 'app/index.html', {'form': form})


def contact(request):
    """
    ビュー : 問い合わせページ
        POSTリクエストの場合
            問い合わせの送信処理を行う
            処理結果に応じて情報を設定し、HttpResponseを返却する

    Parameters
    ----------
    request : HttpRequest
        ページに対するリクエスト

    Returns
    -------
    HttpResponse
        処理結果に応じたレスポンス

    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.send_email()
            form = ImageFileForm()
            messages.success(request, '問い合わせメールの送信が完了しました。')
            return render(request, 'app/index.html', {'form': form})

    return render(request, 'app/contact.html', {'form': form})
