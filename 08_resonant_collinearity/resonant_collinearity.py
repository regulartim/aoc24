import time
from collections import defaultdict
from itertools import chain, permutations

begin = time.time()


###
def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def scale_tuple(t: tuple, factor: int) -> tuple:
    return tuple(factor * elem for elem in t)


def find_antinodes(antennas: list, area: dict, factor: int) -> list:
    result = []
    for a, b in permutations(antennas, 2):
        delta = (a[0] - b[0], a[1] - b[1])
        antinode = add_tuples(a, scale_tuple(delta, factor))
        if antinode in area:
            result.append(antinode)
    if result and factor > 1:
        result += find_antinodes(antennas, area, factor + 1)
    return result


antenna_locations = defaultdict(list)
grid = {}
with open("input.txt") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            if char != ".":
                antenna_locations[char].append((x, y))
            grid[(x, y)] = char

p1_antinodes = [find_antinodes(locs, grid, 1) for locs in antenna_locations.values()]
p2_antinodes = list(antenna_locations.values()) + p1_antinodes
p2_antinodes += [find_antinodes(locs, grid, 2) for locs in antenna_locations.values()]

print(f"Part 1: {len(set(chain(*p1_antinodes)))}")
print(f"Part 2: {len(set(chain(*p2_antinodes)))}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
