from twoCharacters import alternate

import unittest


class testTwoCharacters(unittest.TestCase):
    def test_give_asdcbsdcagfsdbgdfanfghbsfdab(self):
        result = alternate('asdcbsdcagfsdbgdfanfghbsfdab')
        self.assertEqual(result, 8)
    
    def test_give_asvkugfiugsalddlasguifgukvsa(self):
        result = alternate('asvkugfiugsalddlasguifgukvsa')
        self.assertEqual(result, 0)


    def test_give_beabeefeab(self):
        result = alternate('beabeefeab')
        self.assertEqual(result, 5)

    