import unittest
from src.super_fizzbuzz import super_fizzbuzz


class TestSuperFizzBuzz(unittest.TestCase):

    def test_give_3_return_fizz(self):
        num = 3
        expect = 'Fizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_5_return_fizz(self):
        num = 5
        expect = 'Buzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)

    def test_give_15_return_fizz(self):
        num = 15
        expect = 'FizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_9_return_fizz(self):
        num = 9
        expect = 'FizzFizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)

    def test_give_25_return_fizz(self):
        num = 25
        expect = 'BuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_225_return_fizz(self):
        num = 225
        expect = 'FizzFizzBuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)

        
    def test_give_2_return_nofizzbuzz(self):
        num = 2
        expect = 'NoFizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_10000_return_buzzbuzz(self):
        num = 10000
        expect = 'BuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_9999_return_fizzfizz(self):
        num = 9999
        expect = 'FizzFizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_5000_return_buzzbuzz(self):
        num = 5000
        expect = 'BuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_5999_return_nofizzbuzz(self):
        num = 5999
        expect = 'NoFizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_1_return_nofizzbuzz(self):
        num = 1
        expect = 'NoFizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_6_return_fizz(self):
        num = 6
        expect = 'Fizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_9366_return_fizz(self):
        num = 9366
        expect = 'Fizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_2260_return_buzz(self):
        num = 2260
        expect = 'Buzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)

    def test_give_175_return_buzzbuzz(self):
        num = 175
        expect = 'BuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)

    def test_give_6690_return_fizzbuzz(self):
        num = 6690
        expect = 'FizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_9000_return_fizzbuzz(self):
        num = 9195
        expect = 'FizzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_3375_return_fizzfizzbuzzbuzz(self):
        num = 3375
        expect = 'FizzFizzBuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_6075_return_fizzfizzbuzzbuzz(self):
        num = 6075
        expect = 'FizzFizzBuzzBuzz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_108_return_fizzfizz(self):
        num = 108
        expect = 'FizzFizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    
    def test_give_468_return_fizzfizz(self):
        num = 468
        expect = 'FizzFizz'
        result = super_fizzbuzz(num)
        self.assertEqual(result, expect)
    

