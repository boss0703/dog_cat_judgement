from django.urls import path

from app.views import index, contact

#  アプリケーションのルーティング設定

app_name = 'app'
urlpatterns = [
    path('', index, name='index'),
    path('contact', contact, name='contact')
]
