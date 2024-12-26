import time

begin = time.time()

###

with open("input.txt") as file:
    sections = file.read().split("\n\n")

locks, keys = [], []
for s in sections:
    heights = [col.count("#") - 1 for col in zip(*s.splitlines())]
    if s[0] == "#":
        locks.append(heights)
    else:
        keys.append(heights)

count = 0
for lock in locks:
    for key in keys:
        count += all(n + m < 6 for n, m in zip(lock, key))

print(f"Part 1: {count}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
