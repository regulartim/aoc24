import time
from collections import defaultdict
from itertools import combinations

begin = time.time()

###


def find_triplets(conns: dict) -> set:
    result = set()
    for computer, neighbours in conns.items():
        for na, nb in combinations(neighbours, 2):
            if na in conns[nb]:
                result.add(tuple(sorted((computer, na, nb))))
    return result


def bron_kerbosch(clique: set, remaining: set, skip: set, conns: dict):
    if not remaining and not skip:
        yield clique
    else:
        pivot = (remaining | skip).pop()
        for node in remaining - conns[pivot]:
            yield from bron_kerbosch(
                clique | {node},
                remaining & conns[node],
                skip & conns[node],
                conns,
            )
            remaining.remove(node)
            skip.add(node)


connections = defaultdict(set)
with open("input.txt") as file:
    for line in file:
        c, d = line.strip().split("-")
        connections[c].add(d)
        connections[d].add(c)

triplets_with_t = [t for t in find_triplets(connections) if any(c.startswith("t") for c in t)]
cliques = bron_kerbosch(set(), set(connections), set(), connections)
largest_clique = max(cliques, key=len)
password = ",".join(sorted(largest_clique))

print(f"Part 1: {len(triplets_with_t)}")
print(f"Part 2: {password}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
