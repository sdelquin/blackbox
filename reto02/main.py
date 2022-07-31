import random
from collections import defaultdict

CUBE_FACES = 6
YELLOW = '🟨'
BLUE = '🟦'
RED = '🟥'
WHITE = '⬜'
ORANGE = '🟧'
GREEN = '🟩'

COLORS = (YELLOW, BLUE, RED, WHITE, ORANGE, GREEN)


def random_rubik(cube_size: int = 3, colors: tuple[str] = COLORS) -> list[int]:
    if len(colors) != CUBE_FACES:
        raise ValueError('The number of colors must be equal to the number of cube faces')

    cube = []
    color_count = defaultdict(int)
    num_cells_by_face = cube_size**2
    num_cells = num_cells_by_face * CUBE_FACES
    colors = list(colors)

    while len(cube) < num_cells:
        color = random.choice(colors)
        color_count[color] += 1
        if color_count[color] == num_cells_by_face:
            colors.remove(color)
        cube.append(color)

    return cube


print(random_rubik())
