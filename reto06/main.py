disk = (
    (4, 'Unicornio', 2),
    (3, 'Pegasus', 6),
    (1, 'Dragón', 3),
    (5, 'Griffin', 4),
    (2, 'Minotaur', 1),
    (6, 'Quimera', 5),
)


def get_index_by_link(disk: tuple[tuple[int, str, int]], link: int) -> int:
    for i, node in enumerate(disk):
        if node[0] == link:
            return i


def defrag_disk(disk: tuple[tuple[int, str, int]]) -> tuple[tuple[int, str, int]]:
    defragged_disk = []
    disk = list(disk)
    start = sorted(disk, key=lambda t: t[0])[0]
    node = start
    defragged_disk.append(node)
    while node[2] != start[0]:
        index = get_index_by_link(disk, node[2])
        node = disk.pop(index)
        defragged_disk.append(node)
    return tuple(defragged_disk)


assert defrag_disk(disk) == (
    (1, 'Dragón', 3),
    (3, 'Pegasus', 6),
    (6, 'Quimera', 5),
    (5, 'Griffin', 4),
    (4, 'Unicornio', 2),
    (2, 'Minotaur', 1),
)
