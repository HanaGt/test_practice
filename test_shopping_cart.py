import unittest

from shopping_cart import ShoppingCart


class TestShoppingCart(unittest.TestCase):
    def test_empty(self):
        cart = ShoppingCart()
        self.assertEqual(len(cart.cart), 0)