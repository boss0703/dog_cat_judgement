from django.shortcuts import render

from app.forms import ImageFileForm


def index(request):
    form = ImageFileForm()
    return render(request, 'app/index.html', {'form': form})
