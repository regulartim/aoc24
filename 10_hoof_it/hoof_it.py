import time
from collections import deque
from functools import cache

begin = time.time()

###

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


@cache
def neighbours(p: tuple) -> list:
    return [add_tuples(p, d) for d in DIRECTIONS]


def bfs(start: tuple, topo: dict, part1: bool) -> int:
    queue = deque([start])
    visited = set()
    total = 0
    while queue:
        p = queue.popleft()
        if part1 and p in visited:
            continue
        if topo[p] == 9:
            total += 1
            continue
        for n in neighbours(p):
            if topo.get(n, 0) - 1 == topo[p]:
                queue.append(n)
        visited.add(p)
    return total


topographic_map = {}
trailheads = []
with open("input.txt") as file:
    for y, line in enumerate(file):
        for x, num in enumerate(line.strip()):
            if num == "0":
                trailheads.append((x, y))
            topographic_map[(x, y)] = int(num)

print(f"Part 1: {sum(bfs(th, topographic_map, True) for th in trailheads)}")
print(f"Part 2: {sum(bfs(th, topographic_map, False) for th in trailheads)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
