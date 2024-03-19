import unittest

from product import Product

class TestProduct(unittest.TestCase):
    def test_calculat(self):
        product = Product("jhnfjn", 10, 5)
        result = product.calculat()
        self.assertEqual(result, 50)
    
    def test_calculat_zero(self):
        product = Product("jhnfjn", 10, 0)
        result = product.calculat()
        self.assertEqual(result, 0)

    def test_calculat_negative(self):
        product = Product("jhnfjn", 10, -1)
        with self.assertRaises(ValueError)
        result = product.calculat()
       

if __name__ == '__main__':
    unittest.main()