import os
import requests

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
        northside = self.signs[0]["latitude"]
        for sign in self.signs:
            if northside < sign["latitude"]:
                northside = sign["latitude"]
        return northside

    def southside(self):
        southside = self.signs[0]["latitude"]
        for sign in self.signs:
            if southside > sign["latitude"]:
                southside = sign["latitude"]
        return southside

    def eastside(self):
        eastside = self.signs[0]["longitude"]
        for sign in self.signs:
            if eastside < sign["longitude"]:
                eastside = sign["longitude"]
        return eastside

    def westside(self):
        westside = self.signs[0]["longitude"]
        for sign in self.signs:
            if westside > sign["longitude"]:
                westside = sign["longitude"]
        return westside

