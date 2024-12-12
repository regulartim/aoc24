import time
from collections import namedtuple
from functools import cache

begin = time.time()

###

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
Region = namedtuple("Region", ["plant_type", "plots", "perimeter", "sides"])


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def neighbours(p: tuple) -> list:
    return [add_tuples(p, d) for d in DIRECTIONS]


def corner_neighbours(plot: tuple):
    for idx, d1 in enumerate(DIRECTIONS):
        d2 = DIRECTIONS[(idx + 1) % 4]
        na, nb = add_tuples(plot, d1), add_tuples(plot, d2)
        diagonal = add_tuples(plot, add_tuples(d1, d2))
        yield na, diagonal, nb


def count_corners(plots: set) -> int:
    total = 0
    for plot in plots:
        for na, diagonal, nb in corner_neighbours(plot):
            if na in plots and nb in plots and diagonal not in plots:
                total += 1
            if na not in plots and nb not in plots:
                total += 1
    return total


def get_region(start: tuple, garden: dict) -> tuple:
    plant_type = garden[start]
    plots = set()
    perimeter = 0
    q = [start]
    while q:
        plot = q.pop()
        if plot in plots:
            continue
        plots.add(plot)
        for n in neighbours(plot):
            if n not in garden:
                perimeter += 1
                continue
            if garden[n] != plant_type:
                perimeter += 1
                continue
            q.append(n)
    return Region(plant_type, plots, perimeter, count_corners(plots))


garden_map = {}
with open("input.txt") as file:
    for y, line in enumerate(file):
        for x, char in enumerate(line.strip()):
            garden_map[(x, y)] = char

regions, visited_plots = [], set()
for point in garden_map:
    if point in visited_plots:
        continue
    plant_region = get_region(point, garden_map)
    regions.append(plant_region)
    visited_plots.update(plant_region.plots)

print(f"Part 1: {sum(len(r.plots) * r.perimeter for r in regions)}")
print(f"Part 2: {sum(len(r.plots) * r.sides for r in regions)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
