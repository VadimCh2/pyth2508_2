from utils_hw3 import ShoppingCart

class TestShoppingCart:
    def test_add_item_new(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        assert cart.items == [{'name': 'apple', 'price': 10, 'quantity': 3}]

    def test_add_item_existing(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        cart.add_item('apple', 15, 2)
        assert cart.items == [{'name': 'apple', 'price': 15, 'quantity': 5}]

    def test_add_item_multiple_different(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        cart.add_item('bread', 20, 2)
        assert cart.items == [
            {'name': 'apple', 'price': 10, 'quantity': 3},
            {'name': 'bread', 'price': 20, 'quantity': 2},
        ]

    def test_remove_item_existing(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        cart.remove_item('apple')
        assert cart.items == []

    def test_remove_item_not_existing(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        cart.remove_item('bread')
        assert cart.items == [{'name': 'apple', 'price': 10, 'quantity': 3}]

    def test_get_total_empty_cart(self):
        cart = ShoppingCart()
        assert cart.get_total() == 0

    def test_get_total_single_item(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        assert cart.get_total() == 30

    def test_get_total_multiple_items(self):
        cart = ShoppingCart()
        cart.add_item('apple', 10, 3)
        cart.add_item('bread', 20, 2)
        assert cart.get_total() == 70