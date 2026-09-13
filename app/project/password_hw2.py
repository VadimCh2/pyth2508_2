def check_password(password: str) -> bool:
    if len(password) < 8:
        return False

    if ' ' in password:
        return False

    digit_found = False
    letter_found = False
    special_character_found = False

    for current_character in password:
        if current_character.isdigit():
            digit_found = True
        elif current_character.isalpha():
            letter_found = True
        elif not current_character.isspace():
            special_character_found = True

    if not digit_found:
        return False

    if not letter_found:
        return False

    if not special_character_found:
        return False

    return True