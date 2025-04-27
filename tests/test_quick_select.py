import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.quick_select import quick_select
import unittest

class TestQuickSelect(unittest.TestCase):
    """
    Unit tests for the quick_select function.
    """
    def test_normal_array(self):
        """Test with a normal array and k=3."""
        self.assertEqual(quick_select([4, 2, 7, 1, 9, 3], 3), 3)
    
    def test_single_element(self):
        """Test with a single-element array and k=1."""
        self.assertEqual(quick_select([1], 1), 1)
    
    def test_repeated_elements(self):
        """Test with repeated elements and k=2."""
        self.assertEqual(quick_select([5, 5, 5], 2), 5)
    
    def test_two_elements(self):
        """Test with two elements and k=1."""
        self.assertEqual(quick_select([2, 1], 1), 1)
    
    def test_empty_array(self):
        """Test with an empty array."""
        with self.assertRaises(ValueError):
            quick_select([], 1)
    
    def test_invalid_k(self):
        """Test with invalid k (out of bounds)."""
        with self.assertRaises(ValueError):
            quick_select([1, 2, 3], 4)
        with self.assertRaises(ValueError):
            quick_select([1, 2, 3], 0)

if __name__ == "__main__":
    unittest.main()