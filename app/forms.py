from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from app.models import ImageFileModel

from dog_cat_judgement import settings


class ImageFileForm(forms.ModelForm):
    """
    モデルフォーム構成クラス
    画像をアップロードするフォームを作成する
    """
    class Meta:
        model = ImageFileModel
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'custom-file-input', 'onchange': 'previewImage(this);',
                                            'accept': 'image/*,.png,.jpg,.jpeg,.gif', })
        }


class ContactForm(forms.Form):
    """
    フォーム構成クラス
    問い合わせを送信するフォームを作成する
    """
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
        """
        問い合わせメール送信時の処理

        Returns
        -------
        HttpResponse
            送信失敗時のレスポンス
        """
        subject = "お問い合わせ"
        message = self.cleaned_data['message']
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        from_email = '{name} <{email}>'.format(name=name, email=email)

        recipient_list = [settings.EMAIL_HOST_USER, email]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")
