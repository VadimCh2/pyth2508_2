from pytest import fixture

from utils_hw3 import ShoppingCart

@fixture()
def shopingcart() -> ShoppingCart:
    cart = ShoppingCart()
    cart.add_item('apple', 10, 3)
    return cart