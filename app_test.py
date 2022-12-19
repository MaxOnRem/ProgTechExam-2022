import unittest
from app import printParity

class MyTestApp(unittest.TestCase):
    def test_printParity(self):
        parity = printParity()
        self.assertEqual(parity, 'Parity of the week number from beginning of the year is even')

if __name__ == '__main__':
    unittest.main()