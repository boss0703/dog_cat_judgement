from django import forms

from app.models import ImageFileModel


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFileModel
        fields = ('image',)
        labels = {'image': 'ファイルを選択してください(ドロップ可)', }
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input'})
        }
