import unittest
from app import add, subtract

class TestMain(unittest.TestCase):
    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()