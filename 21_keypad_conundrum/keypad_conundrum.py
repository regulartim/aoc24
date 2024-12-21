import time
from collections import deque
from functools import cache

begin = time.time()

###

NUMERIC_LAYOUT = "789 456 123 #0A"
DIRECTIONAL_LAYOUT = "#^A <v>"
DIRECTIONS = {"<": (-1, 0), "v": (0, 1), "^": (0, -1), ">": (1, 0)}


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def neighbours(state: tuple):
    for char, delta in DIRECTIONS.items():
        yield add_tuples(state, delta), char


def parse_layout(layout: str) -> dict:
    result = {}
    for y, line in enumerate(layout.split()):
        for x, char in enumerate(list(line)):
            if char != "#":
                result[(x, y)] = char
    return result


def is_efficient(path: str) -> bool:
    group_conut = 1 + sum(a != b for a, b in zip(path, path[1:]))
    return group_conut <= 2


def shortest_path(start: str, target: str, numeric=False):
    layout = parse_layout(NUMERIC_LAYOUT if numeric else DIRECTIONAL_LAYOUT)
    start_position = [k for k, v in layout.items() if v == start][0]
    queue = deque([(start_position, "")])
    while queue:
        position, path = queue.popleft()
        if layout[position] == target:
            if not is_efficient(path):
                continue
            return path
        for n, direction in neighbours(position):
            if n in layout:
                queue.append((n, path + direction))


@cache
def sequence_length(start: str, target: str, depth: int, numeric=False) -> int:
    sequence = shortest_path(start, target, numeric) + "A"
    if depth == 0:
        return len(sequence)
    return sum(sequence_length(a, b, depth - 1) for a, b in zip("A" + sequence, sequence))


def complexity(code: str, depth: int) -> int:
    sequence_lengths = [sequence_length(a, b, depth, True) for a, b in zip("A" + code, code)]
    return int(code[:-1]) * sum(sequence_lengths)


with open("input.txt") as file:
    codes = file.read().split()

print(f"Part 1: {sum(complexity(c,2) for c in codes)}")
print(f"Part 2: {sum(complexity(c,25) for c in codes)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
