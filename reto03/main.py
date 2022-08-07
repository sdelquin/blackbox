VALID_LENGTH = 16


def hide_numbers(numbers: str | int, char_hide: str = 'x', num_clear_digits: int = 3):
    if len(numbers := str(numbers).replace(' ', '').strip()) != VALID_LENGTH:
        return False

    clear_digits = numbers[-num_clear_digits:]
    mask = char_hide * (VALID_LENGTH - num_clear_digits)
    return mask + clear_digits


assert hide_numbers(1234567890123456) == 'xxxxxxxxxxxxx456'
assert hide_numbers('1234567890123456') == 'xxxxxxxxxxxxx456'
assert hide_numbers('1234 5678 9012 3456') == 'xxxxxxxxxxxxx456'
assert hide_numbers(123) is False

assert hide_numbers(1234567890123456, char_hide='?') == '?????????????456'
assert hide_numbers(1234567890123456, num_clear_digits=4) == 'xxxxxxxxxxxx3456'
