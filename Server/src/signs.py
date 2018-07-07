import os
import requests

BASE_URL = "https://api.what3words.com/v2"
API_KEY = os.environ["RETRAVEL_W3W_API_KEY"]
print("RETRAVEL_W3W_API_KEY", API_KEY)

class Sings():
    def __init__(self, coords_array):
        self.coords_array = coords_array
        self.sings = []
        for coords in self.coords_array:
            print(coords)
