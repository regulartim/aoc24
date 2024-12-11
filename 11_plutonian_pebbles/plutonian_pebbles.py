import time
from functools import cache

begin = time.time()

###


@cache
def count_after(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1
    if stone == 0:
        return count_after(1, iterations - 1)
    s_str = str(stone)
    if len(s_str) % 2 == 0:
        a = int(s_str[: len(s_str) // 2])
        b = int(s_str[len(s_str) // 2 :])
        return count_after(a, iterations - 1) + count_after(b, iterations - 1)
    return count_after(2024 * stone, iterations - 1)


with open("input.txt") as file:
    stone_arrangement = [int(n) for n in file.read().split()]

print(f"Part 1: {sum(count_after(s, 25) for s in stone_arrangement)}")
print(f"Part 2: {sum(count_after(s, 75) for s in stone_arrangement)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
