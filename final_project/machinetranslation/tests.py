import unittest
from translator import english_to_french, french_to_english

class TestEtoF(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        
class TestFtoE(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello') 
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
