# -*- coding: utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)
from firebase import firebase

@app.route('/')
def retravel_url():
    # 1.firebaseからユーザーの移動履歴を取得する
    # Use a service account
    firebase = firebase.FirebaseApplication(os.environ["FIREBASE_DATABASE_URL"], None)
    result = firebase.get('/spajamlast', None)
    print(result)

    # 2.ユーザの移動履歴を引数にSingsをインスタンス化する。
    # sings = Sings(move_history)

    # 3.singsを元に静的地図の画像を作成する。
    # static_map = StaticMap(sings)
    # static_map_url = static_map.url

    # 4.static_map_urlを元にツイート付きの上下地図を合成する。
    # ?未定 Cloudinaryなど使用する？

    # 5.スマホにリクエストを返す
    return 'https://res.cloudinary.com/hwhaxlz5c/image/upload/v1530998382/staticmap.png'

if __name__ == '__main__':
    app.run()