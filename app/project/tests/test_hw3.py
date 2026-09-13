from utils_hw3 import ShoppingCart

class TestShoppingCart:
    def test_add_item_new(self, shopingcart):
        assert shopingcart.items == [{'name': 'apple', 'price': 10, 'quantity': 3}]

    def test_add_item_existing(self, shopingcart):
        shopingcart.add_item('apple', 15, 2)
        assert shopingcart.items == [{'name': 'apple', 'price': 15, 'quantity': 5}]

    def test_add_item_multiple_different(self, shopingcart):

        shopingcart.add_item('bread', 20, 2)
        assert shopingcart.items == [
            {'name': 'apple', 'price': 10, 'quantity': 3},
            {'name': 'bread', 'price': 20, 'quantity': 2},
        ]

    def test_remove_item_existing(self,shopingcart):
        shopingcart.remove_item('apple')
        assert shopingcart.items == []

    def test_remove_item_not_existing(self,shopingcart):
        shopingcart.remove_item('bread')
        assert shopingcart.items == [{'name': 'apple', 'price': 10, 'quantity': 3}]

    def test_get_total_empty_cart(self):
        cart = ShoppingCart()
        assert cart.get_total() == 0

    def test_get_total_single_item(self,shopingcart):
        assert shopingcart.get_total() == 30

    def test_get_total_multiple_items(self,shopingcart):
        shopingcart.add_item('bread', 20, 2)
        assert shopingcart.get_total() == 70