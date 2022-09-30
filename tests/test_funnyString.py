from funnyString import Funnystring

import unittest


class testfunnystring(unittest.TestCase):

    def test_give_bcxz(self):
        result = Funnystring('bcxz')
        self.assertEqual(result, "Not Funny")

    def test_give_acxz(self):
        result = Funnystring('acxz')
        self.assertEqual(result, "Funny")

    def test_give_ivvkxq(self):
        result = Funnystring('ivvkxq')
        self.assertEqual(result, "Not Funny")
