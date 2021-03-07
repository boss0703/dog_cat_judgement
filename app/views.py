from pathlib import Path

from django.shortcuts import render
from django.utils import timezone

from app.forms import ImageFileForm, ContactForm
from app.models import ImageFileModel
from dog_cat_judgement.settings import MEDIA_ROOT


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
            result = judgement(path)

            if result < 0.5:
                context = {'result': round(100-result*100, 2), 'animal': '犬', 'image': image_file.image.name}
            else:
                context = {'result': round(result*100, 2), 'animal': '猫', 'image': image_file.image.name}

            return render(request, 'app/result.html', context)
        else:
            form = ImageFileForm()
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
            return render(request, 'app/index.html', {'form': form})

    return render(request, 'app/contact.html', {'form': form})
