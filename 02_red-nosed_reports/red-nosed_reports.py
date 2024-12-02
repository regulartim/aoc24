import time

begin = time.time()

###


def is_safe(report: list, dampener: bool) -> bool:
    for idx, (a, b) in enumerate(zip(report, report[1:])):
        if a >= b or b - a > 3:
            if not dampener:
                return False
            a_removed = report[:idx] + report[idx + 1 :]
            b_removed = report[: idx + 1] + report[idx + 2 :]
            return is_safe(a_removed, False) or is_safe(b_removed, False)
    return True


with open("input.txt") as file:
    data = [[int(n) for n in line.split()] for line in file.readlines()]

p1_safe = [rep for rep in data if is_safe(rep, False) or is_safe(rep[::-1], False)]
p2_safe = [rep for rep in data if is_safe(rep, True) or is_safe(rep[::-1], True)]

print(f"Part 1: {len(p1_safe)}")
print(f"Part 2: {len(p2_safe)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
