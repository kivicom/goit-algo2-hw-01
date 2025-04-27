import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.min_max import find_min_max
import unittest

class TestFindMinMax(unittest.TestCase):
    """
    Unit tests for the find_min_max function.
    """
    def test_normal_array(self):
        """Test with a normal array of numbers."""
        self.assertEqual(find_min_max([4, 2, 7, 1, 9, 3]), (1, 9))
    
    def test_single_element(self):
        """Test with an array containing a single element."""
        self.assertEqual(find_min_max([1]), (1, 1))
    
    def test_two_elements(self):
        """Test with an array containing two elements."""
        self.assertEqual(find_min_max([2, 1]), (1, 2))
    
    def test_repeated_elements(self):
        """Test with an array containing repeated elements."""
        self.assertEqual(find_min_max([5, 5, 5]), (5, 5))
    
    def test_empty_array(self):
        """Test with an empty array."""
        with self.assertRaises(ValueError):
            find_min_max([])

if __name__ == "__main__":
    unittest.main()