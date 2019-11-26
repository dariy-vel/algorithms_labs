import unittest

from main import angry_beaver


class TestBeavers(unittest.TestCase):
    def test_case_1(self):
        binary_in = "101101101"
        x = 5
        self.assertEqual(3, angry_beaver(binary_in, x))

    def test_case_2(self):
        binary_in = "1111101"
        x = 5
        self.assertEqual(1, angry_beaver(binary_in, x))

    def test_case_3(self):
        binary_in = "110011011"
        x = 5
        self.assertEqual(3, angry_beaver(binary_in, x))

    def test_case_4(self):
        binary_in = "100111011110100100111110110011100101000111100101110010001100111011110100100111110110011100101000110010110000111100101110010001"
        x = 7
        self.assertEqual(5, angry_beaver(binary_in, x))
