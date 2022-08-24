def format_price(price: float | int) -> str:
    if price == int(price):
        return str(int(price))
    return f'{price:.02f}'.replace('.', ',')


assert format_price(8) == '8'
assert format_price(1.0) == '1'
assert format_price(1.5) == '1,50'
assert format_price(2.03) == '2,03'
assert format_price(0.4567) == '0,46'
