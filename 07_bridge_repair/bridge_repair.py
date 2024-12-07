import time

begin = time.time()

###


def evaluate(numbers: list, test_value: int, concat: bool) -> bool:
    *ns, tail = numbers
    if not ns:
        return test_value == tail
    if test_value > tail and evaluate(ns, test_value - tail, concat):
        return True
    if test_value % tail == 0 and evaluate(ns, test_value // tail, concat):
        return True
    tv_str, tail_str = str(test_value), str(tail)
    if concat and len(tv_str) > len(tail_str) and tv_str.endswith(tail_str) and evaluate(ns, int(tv_str[: -len(tail_str)]), concat):
        return True
    return False


with open("input.txt") as file:
    equations = [[int(n.strip(":")) for n in line.split()] for line in file.readlines()]

print(f"Part 1: {sum(e[0] for e in equations if evaluate(e[1:], e[0], concat=False))}")
print(f"Part 2: {sum(e[0] for e in equations if evaluate(e[1:], e[0], concat=True))}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
