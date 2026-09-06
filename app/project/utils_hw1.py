# 1
def calculate_discount(price: float | int, discount: float | float) -> float | int:
    price_with_disc = price * (1 - discount / 100)
    return price_with_disc

# 2
def is_even(number: int) -> bool:
    even = number % 2 == 0
    return even

# 3
def get_full_name(first_name: str, last_name: str) -> str:
    full_name = (f"{first_name} {last_name}")
    return full_name