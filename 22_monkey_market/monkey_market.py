import sys
import time
from collections import defaultdict
from functools import cache

begin = time.time()

###


def derive_secret(n: int) -> int:
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216
    return n


def get_prices(secret: int, depth: int) -> tuple:
    result = []
    for _ in range(depth):
        result.append(secret % 10)
        secret = derive_secret(secret)
    return result, secret


with open("input.txt") as file:
    initial_secrets = list(map(int, file.read().split()))

p1_total = 0
sequence_rating = defaultdict(int)
for s in initial_secrets:
    prices, final_secret = get_prices(s, 2000)
    p1_total += final_secret
    deltas = [b - a for a, b in zip(prices, prices[1:])]
    seen = set()
    for idx, _ in enumerate(deltas[:-4]):
        sequence = tuple(deltas[idx : idx + 4])
        if sequence in seen:
            continue
        seen.add(sequence)
        sequence_rating[sequence] += prices[idx + 4]

print(f"Part 1: {p1_total}")
print(f"Part 2: {max(sequence_rating.values())}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
