from utils_hw1 import calculate_discount, is_even, get_full_name

# 1
def test_calculate_discount_1():
    discount = 20
    price = 100
    expected = 80
    actual = calculate_discount(price, discount)
    assert expected == actual

def test_calculate_discount_2():
    discount = 50
    price = 100
    expected = 50
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_3():
    discount = 0
    price = 100
    expected = 100
    actual = calculate_discount(price, discount)
    assert expected == actual


def test_calculate_discount_4():
    discount = 20
    price = 0
    expected = 0
    actual = calculate_discount(price, discount)
    assert expected == actual



def test_calculate_discount_5():
    discount = 60
    price = 100
    expected = 40
    actual = calculate_discount(price, discount)
    assert expected == actual

# 2

def test_is_even_1():
    number = 4
    expected = True
    actual = is_even(number)
    assert expected is actual


def test_is_even_2():
    number = 3
    expected = False
    actual = is_even(number)
    assert expected is actual


def test_is_even_3():
    number = -4
    expected = True
    actual = is_even(number)
    assert expected is actual



def test_is_even_4():
    number = -3
    expected = False
    actual = is_even(number)
    assert expected is actual


def test_is_even_5():
    number = 0
    expected = True
    actual = is_even(number)
    assert expected is actual


# 3

def test_get_full_name_1():
    first_name = "Кіріл"
    last_name = "Ободовський"
    expected = f"{first_name} {last_name}"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_2():
    first_name = "Кi"
    last_name = "Ободовський"
    expected = f"{first_name} {last_name}"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_3():
    first_name = "Кірілдужекрутийпацик"
    last_name = "Ободовський"
    expected = f"{first_name} {last_name}"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_4():
    first_name = "К"
    last_name = "Ободовський"
    expected = f"{first_name} {last_name}"
    actual = get_full_name(first_name, last_name)
    assert expected == actual


def test_get_full_name_5():
    first_name = "К"
    last_name = "О"
    expected = f"{first_name} {last_name}"
    actual = get_full_name(first_name, last_name)
    assert expected == actual
