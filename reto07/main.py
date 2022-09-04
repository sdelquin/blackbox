from core import base


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    return f'#{red:02x}{green:02x}{blue:02x}'


assert rgb_to_hex(82, 31, 130) == '#521f82'
assert rgb_to_hex(255, 0, 0) == '#ff0000'

assert base.dec_to_base(82, 16) == '52'
assert base.dec_to_base(31, 16) == '1f'
assert base.dec_to_base(130, 16) == '82'

assert base.dec_to_base(255, 16) == 'ff'
assert base.dec_to_base(0, 16) == '0'

assert base.dec_to_base(500, 2) == '111110100'
assert base.dec_to_base(500, 8) == '764'

# assert base.dec_to_base(0, 7)  # NotImplementedError
