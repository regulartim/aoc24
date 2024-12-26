import time
from functools import cache
from itertools import pairwise

begin = time.time()

###

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


@cache
def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def walk(position: tuple, dir_idx: int, lab: dict) -> set:
    visited_states = set()
    path = []
    while position in lab:
        state = (position, dir_idx)
        if state in visited_states:
            return None
        visited_states.add(state)
        path.append(state)
        new_pos = add_tuples(position, DIRECTIONS[dir_idx])
        if lab.get(new_pos) == "#":
            dir_idx = (dir_idx + 1) % 4
            continue
        position = new_pos
    return path


def test_obstructions(path: list, lab: dict) -> set:
    simulation_starts = {}
    successful_obstructions = set()
    for start_state, (pos, _) in pairwise(path):
        start_state = simulation_starts.setdefault(pos, start_state)
        if walk(*start_state, lab | {pos: "#"}) is None:
            successful_obstructions.add(pos)
    return successful_obstructions


lab_map = {}
starting_position = None
with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line):
            lab_map[(x, y)] = char
            starting_position = (x, y) if char == "^" else starting_position

guard_path = walk(starting_position, 0, lab_map)

print(f"Part 1: {len({pos for pos, _ in guard_path})}")
print(f"Part 2: {len(test_obstructions(guard_path, lab_map))}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
