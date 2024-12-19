import time
from collections import defaultdict
from functools import cache

begin = time.time()

###


@cache
def count_arrangemnts(design: str, patterns: frozenset) -> int:
    if not design:
        return 1
    counter = 0
    for candidate in patterns:
        if design.startswith(candidate):
            counter += count_arrangemnts(design.removeprefix(candidate), patterns)
    return counter


with open("input.txt") as file:
    sections = file.read().split("\n\n")

towel_patterns = frozenset(sections[0].split(", "))
towel_designs = sections[1].splitlines()
arrangement_counts = [count_arrangemnts(d, towel_patterns) for d in towel_designs]

print(f"Part 1: {sum(c > 0 for c in arrangement_counts)}")
print(f"Part 2: {sum(arrangement_counts)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
