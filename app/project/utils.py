def concatenate(string_1, string_2):
    print(123)
    return str(string_1) + str(string_2)
def concatenate_two_strings(string_1: str, string_2: str = '123') -> str:
    result = str(string_1) + str(string_2)
    # print(result)
    return result


result = concatenate(55, 66)
print(result)
def is_number_positive(number: int | float) -> bool:
    result = number > 0.1
    return result