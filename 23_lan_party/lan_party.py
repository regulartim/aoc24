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


def bron_kerbosch(r, p, x, conns):
    if not p and not x:
        return r
    cliques = []
    for v in list(p):
        cliques.append(bron_kerbosch(r | {v,}, p & conns[v], x & conns[v], conns))
        p.remove(v)
        x.add(v)
    return max(cliques, key=len) if cliques else {}


connections = defaultdict(set)
with open("input.txt") as file:
    for line in file:
        c, d = line.strip().split("-")
        connections[c].add(d)
        connections[d].add(c)

triplets_with_t = [t for t in find_triplets(connections) if any(c.startswith("t") for c in t)]
maximum_clique = bron_kerbosch(set(),set(connections),set(), connections)
password = ",".join(sorted(maximum_clique))

print(f"Part 1: {len(triplets_with_t)}")
print(f"Part 2: {password}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
