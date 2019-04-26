import unittest

from main import number_to_string

class TestNumberToString(unittest.TestCase):
    def test_number_to_string_123(self):
        result = number_to_string(123)
        self.assertEqual(result, '123')
    
    def test_number_to_string_999(self):
        result = number_to_string(999)
        self.assertEqual(result, '999')

if __name__ == '__main__':
    unittest.main()
