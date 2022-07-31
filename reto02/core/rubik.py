import random
from collections import defaultdict

from .colors import COLORS


class RubikFace:
    def __init__(self, size):
        self.size = size
        self.boxes = []

    def add_box(self, color):
        self.boxes.append(color)

    def __len__(self):
        return len(self.boxes)

    def __str__(self):
        buf = []
        for i, box in enumerate(self.boxes):
            buf.append(box)
            if (i + 1) % self.size == 0:
                buf.append('\n')
        return ''.join(buf)


class RubikCube:
    num_faces = 6

    def __init__(self, cube_size: int = 3, colors: tuple[str] = COLORS):
        if len(colors) != self.num_faces:
            raise ValueError(
                'The number of colors must be equal to the number of cube faces'
            )
        self.cube = []
        self.cube_size = cube_size
        self.colors = colors
        self.num_cells_by_face = cube_size**2

    def gen_random(self):
        colors = list(self.colors)
        color_count = defaultdict(int)

        for _ in range(self.num_faces):
            face = RubikFace(self.cube_size)
            while len(face) < self.num_cells_by_face:
                color = random.choice(colors)
                color_count[color] += 1
                if color_count[color] == self.num_cells_by_face:
                    colors.remove(color)
                face.add_box(color)
            self.cube.append(face)

    def __str__(self):
        return '\n'.join(str(f) for f in self.cube)
