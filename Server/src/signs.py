import os
import requests

BASE_URL = "https://api.what3words.com/v2"
API_KEY = os.environ["RETRAVEL_W3W_API_KEY"]
print("RETRAVEL_W3W_API_KEY", API_KEY)
SIGN_NUMBER = 10

class Signs():
    # 緯度・経度の順番
    def __init__(self, coords_array):
        self.coords_array = coords_array
        self.signs = []
        times = len(self.coords_array)//SIGN_NUMBER # 何個おきに取得するか
        cnt = 1
        for coords in self.coords_array:
            if SIGN_NUMBER*times >= cnt and cnt%times == 0:
                self.signs.append(coords)
            cnt = cnt + 1

    def northside(self):
        northside = self.signs[0][0]
        for sign in self.signs:
            if northside < sign[0]:
                northside = sign[0]
        return northside

    def southside(self):
        southside = self.signs[0][0]
        for sign in self.signs:
            if southside > sign[0]:
                southside = sign[0]
        return southside

    def eastside(self):
        eastside = self.signs[0][1]
        for sign in self.signs:
            if eastside < sign[1]:
                eastside = sign[1]
        return eastside

    def westside(self):
        westside = self.signs[0][1]
        for sign in self.signs:
            if westside > sign[1]:
                westside = sign[1]
        return westside

