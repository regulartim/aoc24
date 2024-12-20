import time
from collections import Counter, deque
from itertools import combinations

begin = time.time()

###
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def neighbours(state: tuple):
    for d in DIRECTIONS:
        yield add_tuples(state, d)


def build_dist_map(ref_point: tuple, track: set) -> dict:
    result = {}
    q = deque([(ref_point, 0)])
    while q:
        p, dist = q.popleft()
        if p in result:
            continue
        result[p] = dist
        for n in neighbours(p):
            if n not in track:
                continue
            q.append((n, dist + 1))
    return result


def count_cheats(distances: dict, cutoff: int) -> int:
    counter = {2: 0, 20: 0}
    for (p, p_dist), (q, q_dist) in combinations(distances.items(), 2):
        dist_delta = abs(p[0] - q[0]) + abs(p[1] - q[1])
        if abs(p_dist - q_dist) < dist_delta + cutoff:
            continue
        if dist_delta <= 2:
            counter[2] += 1
        if dist_delta <= 20:
            counter[20] += 1
    return counter


finish, racetrack = (0, 0), set()
with open("input.txt") as file:
    for y_coord, line in enumerate(file):
        for x_coord, char in enumerate(line):
            if char == "#":
                continue
            if char == "E":
                finish = (x_coord, y_coord)
            racetrack.add((x_coord, y_coord))

dist_map = build_dist_map(finish, racetrack)
cheat_counts = count_cheats(dist_map, 100)

print(f"Part 1: {cheat_counts[2]}")
print(f"Part 2: {cheat_counts[20]}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
