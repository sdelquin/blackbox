import random
import string
from typing import Iterable

PASSWORD_CHAR_COLLECTIONS = (
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.digits,
    string.punctuation,
)


def get_random_char(collections: Iterable[str] = PASSWORD_CHAR_COLLECTIONS) -> str:
    while True:
        for colection in collections:
            yield random.choice(colection)


def gen_password(length: int, min_length=4) -> str:
    length = max(length, min_length)
    grc = get_random_char()
    return ''.join(random.sample([next(grc) for _ in range(length)], length))


def check_password(
    password: str,
    desired_length: int,
    desired_collections: Iterable[str] = PASSWORD_CHAR_COLLECTIONS,
) -> bool:
    if len(password) != desired_length:
        return False
    check_collections = [False] * len(desired_collections)
    for char in password:
        for i, collection in enumerate(desired_collections):
            if char in collection:
                check_collections[i] = True
                break
        if all(check_collections):
            return True
    return False


assert check_password(gen_password(10), 10)
assert check_password(gen_password(6), 6)
assert check_password(gen_password(4), 4)
