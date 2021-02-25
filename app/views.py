from django.shortcuts import render
from django.utils import timezone

from app.forms import ImageFileForm
from app.models import ImageFileModel


def index(request):
    if request.method == 'POST':
        form = ImageFileForm(request.POST or None)
        if form.is_valid():
            image_file = ImageFileModel()
            image_file.image = request.FILES['image']
            image_file.published_date = timezone.now()

            image_file.save()
            form.save()

            from app.judgement import judgement
            value = judgement(request.FILES['image'])
            print(value)

            return render(request, 'app/result.html',)
    else:
        form = ImageFileForm()
        return render(request, 'app/index.html', {'form': form})
