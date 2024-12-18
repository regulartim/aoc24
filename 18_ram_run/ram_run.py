import heapq
import time
from functools import cache

begin = time.time()

###

GRID_SIZE = 70
BYTE_COUNT = 1024

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


@cache
def neighbours(state: tuple) -> list:
    result = []
    for d in DIRECTIONS:
        x, y = add_tuples(state, d)
        if 0 <= x <= GRID_SIZE and 0 <= y <= GRID_SIZE:
            result.append((x, y))
    return result


def shortest_path(start: tuple, finish: tuple, falling: set) -> int:
    q, visited = [(0, start)], set()
    while q:
        distance, state = heapq.heappop(q)
        if state in visited:
            continue
        visited.add(state)
        if state == finish:
            return distance
        for n in neighbours(state):
            if n in visited:
                continue
            if n in falling:
                continue
            heapq.heappush(q, (distance + 1, n))
    return None


def find_blocking_byte(start: tuple, finish: tuple, falling: list) -> tuple:
    left, right = BYTE_COUNT, len(falling)
    while left < right - 1:
        middle = (left + right) // 2
        if shortest_path(start, finish, set(falling[:middle])) is None:
            right = middle
        else:
            left = middle
    return falling[left]


incomming = []
with open("input.txt") as file:
    for line in file:
        incomming.append(tuple(map(int, line.split(","))))

top_left, bottom_right = ((0, 0), (GRID_SIZE, GRID_SIZE))


print(f"Part 1: {shortest_path(top_left, bottom_right, set(incomming[:BYTE_COUNT]))}")
print(f"Part 2: {find_blocking_byte(top_left, bottom_right, incomming)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
