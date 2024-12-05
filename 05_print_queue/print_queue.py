import time
from collections import defaultdict

begin = time.time()

###


def sort_update(update: list, succs: dict) -> bool:
    for idx, page in enumerate(update):
        if succs[page].intersection(update[:idx]):
            update[idx], update[idx - 1] = update[idx - 1], update[idx]
            break
    else:
        return True
    sort_update(update, succs)
    return False


updates = []
successors = defaultdict(set)
with open("input.txt") as file:
    sections = file.read().strip().split("\n\n")
    for line in sections[0].split():
        a, b = line.split("|")
        successors[int(a)].add(int(b))
    for line in sections[1].split():
        updates.append([int(n) for n in line.split(",")])

was_sorted = [sort_update(u, successors) for u in updates]

print(f"Part 1: {sum(u[len(u) // 2] for u, w in zip(updates, was_sorted) if w)}")
print(f"Part 2: {sum(u[len(u) // 2] for u, w in zip(updates, was_sorted) if not w)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
