# dog_cat_judgement
* アップロードした画像が犬なのか猫なのか機械学習を利用して判別するサイトです。
* Herokuを利用して [こちら](https://dogcatjudgement.herokuapp.com/) で公開しています。
* 無料枠なので重かったり止まったりすることがあります。

![](https://user-images.githubusercontent.com/58591437/126023278-162d3124-f4b4-463c-83b8-5ad175977348.png)
![](https://user-images.githubusercontent.com/58591437/126023291-b9b457ca-db77-4c9b-8314-18d9ece74aaa.png)

## 目次
 - [環境](#環境)
 - [セットアップ](#セットアップ)

## 環境
* python：3.7.9
* Django：3.1.4
* Keras：2.4.3
* TensorFlow：1.15.3 ※ Herokuで公開するにあたってバージョンを下げました。
* whitenoise：5.2.0

## セットアップ
requirements.txtから必要なライブラリをインストール
```
$ pip install -r requirements.txt
```
settings.py修正(local_settings.pyを作るといいと思います)
```python
# EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_USER = '自分のメールアドレス'
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_PASSWORD = 'メールアドレスのパスワード(二段階認証のアプリパスワード等)'
# EMAIL_PORT = os.environ['EMAIL_PORT']
EMAIL_PORT = 587
# EMAIL_USE_TLS = os.environ['EMAIL_USE_TLS']
EMAIL_USE_TLS = True
# SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'シークレットキー'
```
サーバー起動
```
$ python manage.py runserver
```

