BASE_DIGITS = {'2': '01', '8': '01234567', '16': '0123456789abcdef'}


def dec_to_base(number: int, base: int = 10):
    result = []
    quotient = number
    while True:
        quotient, remainder = divmod(quotient, base)
        result.append(remainder)
        if quotient < base:
            break
    if quotient > 0:
        result.append(quotient)
    try:
        return ''.join(BASE_DIGITS[str(base)][d] for d in result[::-1])
    except KeyError:
        raise NotImplementedError(f'Base {base} is not implemented')
