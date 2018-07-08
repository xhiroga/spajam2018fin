# -*- coding: utf-8 -*-

import json, os, sys, unittest
sys.path.append("src/")
from signs import Signs

f = open('tests/json/spajamlast-coodinates-export.json')
jl = json.load(f)
COORDS_HISOTRY = []
for key in jl.keys():
    COORDS_HISOTRY.append(jl[key])

class SingsTest(unittest.TestCase):
    # 11個以上の引数を受け取っても10個にサマって返す。
    def test_right_sings(self):
        s = Signs(COORDS_HISOTRY)
        expect_count = 10
        actual_count = len(s.signs)
        self.assertEqual(expect_count, actual_count)

    def test_northside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 37.785834
        actual = s.northside()
        self.assertEqual(expect, actual)

    def test_southside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 37.785834
        actual = s.southside()
        self.assertEqual(expect, actual)

    def test_eastside(self):
        s = Signs(COORDS_HISOTRY)
        expect = -122.406417
        actual = s.eastside()
        self.assertEqual(expect, actual)

    def test_westside(self):
        s = Signs(COORDS_HISOTRY)
        expect = -122.406417
        actual = s.westside()
        self.assertEqual(expect, actual)
