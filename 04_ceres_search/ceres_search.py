import time

begin = time.time()

###

ADJACENCY = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def diagonals(rows: list) -> list:
    pad_size = len(rows) - 1
    padded_fwd, padded_bwd = [], []
    for idx, r in enumerate(rows):
        padded_fwd.append("." * (pad_size - idx) + r + "." * idx)
        padded_bwd.append("." * idx + r + "." * (pad_size - idx))
    fwd_diags = ["".join(col) for col in zip(*padded_fwd)]
    bwd_diags = ["".join(col) for col in zip(*padded_bwd)]
    return fwd_diags + bwd_diags


def xmas_search(rows: list) -> int:
    counter = 0
    cols = ["".join(col) for col in zip(*rows)]
    diags = diagonals(
        rows,
    )
    for line in rows + cols + diags:
        counter += line.count("XMAS")
        counter += line.count("SAMX")
    return counter


def x_mas_search(rows: list) -> int:
    counter = 0
    coordinates = {
        (x, y): char for y, row in enumerate(rows) for x, char in enumerate(row)
    }
    for coord, char in coordinates.items():
        if char != "A":
            continue
        neighbours = [
            coordinates.get(p, ".")
            for p in [add_tuples(coord, delta) for delta in ADJACENCY]
        ]
        if not neighbours.count("M") == neighbours.count("S") == 2:
            continue
        if neighbours[0] == neighbours[-1]:
            continue
        counter += 1
    return counter


with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

print(f"Part 1: {xmas_search(lines)}")
print(f"Part 2: {x_mas_search(lines)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
