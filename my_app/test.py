import unittest
from app import add, subtract
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

class TestMain(unittest.TestCase):
    def test_add(self):
        result = add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = subtract(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
    app.run(debug=True, host='0.0.0.0', port=8000)