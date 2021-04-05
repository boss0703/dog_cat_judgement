from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from app.models import ImageFileModel
from dog_cat_judgement import local_settings


class ImageFileForm(forms.ModelForm):
    class Meta:
        model = ImageFileModel
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input', 'onchange': 'previewImage(this);',
                                            'accept': 'image/*,.png,.jpg,.jpeg,.gif', })
        }


class ContactForm(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前",
        }),
    )
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    message = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        recipient_list = [local_settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
