# test_collatz.py
import unittest
from collatz import steps

class TestCollatz(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(steps(1), 0)
        self.assertEqual(steps(2), 1)
        self.assertEqual(steps(3), 7)
        self.assertEqual(steps(12), 9)
    
    def test_invalid_zero(self):
        with self.assertRaises(ValueError) as cm:
            steps(0)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed")
    
    def test_negative_number(self):
        with self.assertRaises(ValueError) as cm:
            steps(-5)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed")

if __name__ == '__main__':
    unittest.main()
