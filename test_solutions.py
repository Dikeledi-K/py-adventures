# test_solutions.py
import unittest
from solutions import *

class TestSolutions(unittest.TestCase):
    
    def test_mastermind(self):
        self.assertEqual(mastermind("RGBY", "RGBY"), (4, 0))
        self.assertEqual(mastermind("RGBY", "YRGB"), (0, 4))
        self.assertEqual(mastermind("RGBY", "RRGG"), (2, 0))
        
    def test_to_roman(self):
        self.assertEqual(to_roman(3), "III")
        self.assertEqual(to_roman(9), "IX")
        self.assertEqual(to_roman(2023), "MMXXIII")
        
    def test_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 3), 2)
        self.assertEqual(binary_search(arr, 6), -1)
        self.assertEqual(binary_search([], 1), -1)
        
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
        
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome(""))
        
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([], [1, 2]), [1, 2])
        self.assertEqual(merge_sorted_arrays([1], []), [1])
        
    def test_validate_password(self):
        self.assertTrue(validate_password("P@ssw0rd"))
        self.assertFalse(validate_password("password"))
        self.assertFalse(validate_password("P@ssword"))
        
    def test_cash_register(self):
        self.assertEqual(cash_register(19.5, 20.0), {"50C": 1})
        self.assertEqual(cash_register(45.8, 50.0), {"R2": 2, "20C": 1})
        self.assertEqual(cash_register(10.0, 20.0), {"R10": 1})
        
    def test_are_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertTrue(are_anagrams("", ""))
        
    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix([""]), "")
        
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("2 + 3"), 5.0)
        self.assertEqual(evaluate_expression("2 + 3 * 4"), 14.0)
        self.assertEqual(evaluate_expression("10 - 2 / 2"), 9.0)
        
    def test_find_duplicates(self):
        self.assertEqual(sorted(find_duplicates([1, 2, 3, 2, 4, 1])), [1, 2])
        self.assertEqual(find_duplicates([1, 2, 3]), [])
        self.assertEqual(find_duplicates([]), [])
        
    def test_print_pascal_triangle(self):
        self.assertEqual(print_pascal_triangle(3), "  1\n 1 1\n1 2 1")
        self.assertEqual(print_pascal_triangle(1), "1")
        
    def test_print_diamond_pattern(self):
        self.assertEqual(print_diamond_pattern(2), " *\n***\n *")
        self.assertEqual(print_diamond_pattern(3), "  *\n ***\n*****\n ***\n  *")
        
    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
    unittest.main()