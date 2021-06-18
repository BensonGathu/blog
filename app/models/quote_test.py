import unittest
import quote

Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    def setUp(self):
        """Will run before every test"""
        self.new_quote = Quote(1,"Benson","Man is wise")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))

    
if __name__ == '__main__':
    unittest.main()