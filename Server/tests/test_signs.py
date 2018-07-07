import os, sys, unittest
sys.path.append("src/")
from sings import Sings

class SingsTest(unittest.TestCase):
    def test_right_sings(self):
        coords = [(51.432393,-0.348023),(51.432393,-0.348023)]
        s = Signs(coords)
        expect = [
            {
                "lng": -0.203607,
                "lat": 51.521238
            },{
                "lng": -0.203607,
                "lat": 51.521238
            },
        ]
        actual = s.sings
        self.assertEqual(expected, actual)