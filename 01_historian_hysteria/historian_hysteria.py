import time
from collections import Counter

begin = time.time()

###

left_list, right_list = [], []
with open("input.txt") as file:
    for line in file.readlines():
        l, r = line.split()
        left_list.append(int(l))
        right_list.append(int(r))

left_list, right_list = sorted(left_list), sorted(right_list)
right_counter = Counter(right_list)
distances = [abs(l - r) for l, r in zip(left_list, right_list)]
similarity_scores = [l * right_counter[l] for l in left_list]

print(f"Part 1: {sum(distances)}")
print(f"Part 2: {sum(similarity_scores)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
