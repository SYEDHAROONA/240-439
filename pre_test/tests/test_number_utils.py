from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_4_7_11_is_prime(self):
        prime_list = [4, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_79_83_89_is_prime(self):
        prime_list = [79, 83, 89]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_809_811_821_is_prime(self):
        prime_list = [809, 811, 821]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    
    def test_give_983_991_997_is_prime(self):
        prime_list = [983, 991, 997]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)