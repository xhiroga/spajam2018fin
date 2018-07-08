# -*- coding: utf-8 -*-

import os, sys, unittest
sys.path.append("src/")
from signs import Signs

COORDS_HISOTRY = [
    (1, 50),
    (2, 49),
    (3, 48),
    (4, 47),
    (5, 46),
    (6, 45),
    (7, 44),
    (8, 43),
    (9, 42),
    (10, 41),
    (11, 40)
]

class SingsTest(unittest.TestCase):
    # 11個以上の引数を受け取っても10個にサマって返す。
    def test_right_sings(self):
        s = Signs(COORDS_HISOTRY)
        expect_count = 10
        actual_count = len(s.signs)
        self.assertEqual(expect_count, actual_count)

    def test_northside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 10
        actual = s.northside()
        self.assertEqual(expect, actual)

    def test_southside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 1
        actual = s.southside()
        self.assertEqual(expect, actual)

    def test_eastside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 50
        actual = s.eastside()
        self.assertEqual(expect, actual)

    def test_westside(self):
        s = Signs(COORDS_HISOTRY)
        expect = 41
        actual = s.westside()
        self.assertEqual(expect, actual)
