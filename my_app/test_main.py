import unittest
from app import add, subtract
import allure

class TestMain(unittest.TestCase):
    @allure.title("Test add")
    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)
    
    @allure.title("Test sub")
    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
