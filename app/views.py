from pathlib import Path

from django.contrib import messages
from django.shortcuts import render
from django.utils import timezone

from app.forms import ImageFileForm, ContactForm
from app.models import ImageFileModel
from dog_cat_judgement.settings import MEDIA_ROOT

from logging import getLogger, StreamHandler, DEBUG

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


def index(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST or None, request.FILES)
        if form.is_valid():
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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.send_email()
            form = ImageFileForm()
            messages.success(request, '問い合わせメールの送信が完了しました。')
            return render(request, 'app/index.html', {'form': form})

    return render(request, 'app/contact.html', {'form': form})
