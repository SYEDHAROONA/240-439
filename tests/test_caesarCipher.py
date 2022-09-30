from caesarCipher import caesarCipher

import unittest


class testcaesarcipher(unittest.TestCase):

    def test_give_string_AlwaysLookontheBrightSideofLife_key5(self):
        result = caesarCipher('Always-Look-on-the-Bright-Side-of-Life', 5)
        self.assertEqual(result, 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj')

    def test_give_string_middleOutz_key2(self):
        result = caesarCipher('middle-OutZ', 2)
        self.assertEqual(result, 'okffng-QwvB')

    def test_give_abcdefghijklmnopqrstuvwxyz_step_26_return_abcdefghijklmnopqrstuvwxyz(self):
        result = caesarCipher('abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(result, 'abcdefghijklmnopqrstuvwxyz')
    
