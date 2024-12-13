import re
import time

import numpy as np

begin = time.time()

###

P2_DELTA = 10000000000000


def tokens_to_spend(machine: str, part2: bool) -> int:
    delta = P2_DELTA if part2 else 0
    xa, ya, xb, yb, xp, yp = map(int, re.findall(r"\d+", machine))
    coeff_matrix = np.array([[xa, xb], [ya, yb]])
    dependent_vals = np.array([xp + delta, yp + delta])
    result = tuple(map(round, np.linalg.solve(coeff_matrix, dependent_vals)))
    if not all(np.dot(coeff_matrix, result) == dependent_vals):
        return 0
    return 3 * result[0] + result[1]


with open("input.txt") as file:
    machines = file.read().split("\n\n")

print(f"Part 1: {sum(tokens_to_spend(m, False) for m in machines)}")
print(f"Part 2: {sum(tokens_to_spend(m, True) for m in machines)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
