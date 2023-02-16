from whiteboard import *
# change whiteboard to python file name, you can change * to function name
import unittest

class CalculatorTest(unittest.TestCase):

    def test_vowel_binary(self):
        result1 = vowel_binary("abceios")
        self.assertEqual(result1, "1001110")
        result2 = vowel_binary("aeiou, abc")
        self.assertEqual(result2, "1111100100")
        
    def test_no_occurences(self):
        result = vowel_binary('bcd fg')
        self.assertEqual(result, '000000')

unittest.main()