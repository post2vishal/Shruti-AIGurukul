import unittest
from scripts.shruti_ai import grok_validate

class TestShrutiAI(unittest.TestCase):
    def test_validate_correct(self):
        self.assertTrue(grok_validate("air pollution harms lungs"))
    def test_validate_incorrect(self):
        self.assertFalse(grok_validate("wrong fact"))

if __name__ == '__main__':
    unittest.main()
