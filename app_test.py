import unittest
from app import GreeterFun

class MyTestApp(unittest.TestCase):
    def test_default_greeting(self):
        greeter = GreeterFun()
        self.assertEqual(greeter, 'Hi there from pipeline app!')

if __name__ == '__main__':
    unittest.main()