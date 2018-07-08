# -*- coding: utf-8 -*-
import json, os, sys
from flask import Flask
app = Flask(__name__)
import pyrebase
sys.path.append("src/")
from signs import Signs

config = {
  "apiKey": os.environ["FIREBASE_API_KEY"],
  "authDomain": os.environ["FIREBASE_AUTH_DOMAIN"],
  "databaseURL": os.environ["FIREBASE_DATABASE_URL"],
  "storageBucket": os.environ["FIREBASE_STORAGE_BUCKET"]
}
firebase = pyrebase.initialize_app(config)

@app.route('/')
def retravel_url():
    # 1.firebaseからユーザーの移動履歴を取得する
    # db = firebase.database()
    # ref = db.child("spajamlast").child("coodinates").get()
    # print(ref.val())
    f = open('tests/json/spajamlast-coodinates-export.json')
    jl = json.load(f)
    COORDS_HISOTRY = []
    for key in jl.keys():
        COORDS_HISOTRY.append(jl[key])

    # 2.ユーザの移動履歴を引数にSingsをインスタンス化する。
    signs = Signs(COORDS_HISOTRY)

    # 3.singsを元に静的地図の画像を作成する。
    # static_map = StaticMap(sings)
    # static_map_url = static_map.url

    # 4.static_map_urlを元にツイート付きの上下地図を合成する。
    # ?未定 Cloudinaryなど使用する？

    # 5.スマホにリクエストを返す
    return 'https://res.cloudinary.com/hwhaxlz5c/image/upload/v1530998382/staticmap.png'

if __name__ == '__main__':
    app.run()