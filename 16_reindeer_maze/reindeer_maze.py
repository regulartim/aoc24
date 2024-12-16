import heapq
import time
from collections import defaultdict

begin = time.time()

###

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def neighbours(state: tuple) -> list:
    x, y, d = state
    return [(1, *add_tuples((x, y), DIRECTIONS[d]), d), (1000, x, y, (d + 1) % 4), (1000, x, y, (d - 1) % 4)]


def shortest_path(start: tuple, finish: tuple, maze: set) -> int:
    shortest_paths = []
    parents = defaultdict(list)
    q, visited = [(0, start)], set()
    while q:
        distance, state = heapq.heappop(q)
        visited.add(state)
        if (state[0], state[1]) == finish:
            if shortest_paths and distance > shortest_paths[-1][0]:
                return shortest_paths[-1][0], parents
            shortest_paths.append((distance, []))
        for n_dist, x, y, d in neighbours(state):
            if (x, y, d) in visited:
                continue
            if (x, y) not in maze:
                continue
            parents[(x, y, d)].append(state)
            heapq.heappush(q, (distance + n_dist, (x, y, d)))
    return -1


def count_path_tiles(parents, finish):
    seen = set()
    q = set()
    for dir_idx in range(4):
        q.update(parents[(*finish, dir_idx)])
    while q:
        x, y, d = q.pop()
        q.update(parents[x, y, d])
        seen.add((x, y))
    return len(seen)


reindeer_maze = set()
start_state, end_tile = (0, 0, 0), (0, 0)
with open("input.txt") as file:
    for y_coord, line in enumerate(file):
        for x_coord, char in enumerate(line):
            if char == "#":
                continue
            if char == "S":
                start_state = (x_coord, y_coord, 0)
            if char == "E":
                end_tile = (x_coord, y_coord)
            reindeer_maze.add((x_coord, y_coord))

shortest_path_lengh, parent_tiles = shortest_path(start_state, end_tile, reindeer_maze)

print(f"Part 1: {shortest_path_lengh}")
print(f"Part 2: {count_path_tiles(parent_tiles, end_tile)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
