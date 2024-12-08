import time

begin = time.time()

###

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def walk(position: tuple, dir_idx: int, lab: dict) -> set:
    visited_states = set()
    while position in lab:
        if (position, dir_idx) in visited_states:
            return None
        visited_states.add((position, dir_idx))
        new_pos = add_tuples(position, DIRECTIONS[dir_idx])
        if lab.get(new_pos) == "#":
            dir_idx = (dir_idx + 1) % 4
            continue
        position = new_pos
    return {pos for pos, dir_idx in visited_states}


def test_obstruction(obs_pos: tuple, start_pos: tuple, lab: dict) -> bool:
    if obs_pos == start_pos:
        return False
    lab[obs_pos] = "#"
    result = walk(start_pos, 0, lab)
    lab[obs_pos] = "."
    return result is None


lab_map = {}
starting_position = None
with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        for x, char in enumerate(line):
            lab_map[(x, y)] = char
            starting_position = (x, y) if char == "^" else starting_position

visited_positions = walk(starting_position, 0, lab_map)
obstruction_positions = [pos for pos in visited_positions if test_obstruction(pos, starting_position, lab_map)]

print(f"Part 1: {len(visited_positions)}")
print(f"Part 2: {len(obstruction_positions)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
