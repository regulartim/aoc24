import time

begin = time.time()

###


def evaluate(numbers: list, test_value: int, concat: bool) -> bool:
    *ns, tail = numbers
    if not ns:
        return tail == test_value
    new_test_values = [test_value - tail]
    if test_value % tail == 0:
        new_test_values.append(test_value // tail)
    if concat and str(test_value).endswith(str(tail)):
        unconcated = str(test_value).removesuffix(str(tail))
        new_test_values.append(int(unconcated) if unconcated else 0)
    return any(evaluate(ns, tv, concat) for tv in new_test_values)


with open("input.txt") as file:
    equations = [[int(n.strip(":")) for n in line.split()] for line in file.readlines()]

print(f"Part 1: {sum(e[0] for e in equations if evaluate(e[1:], e[0], concat=False))}")
print(f"Part 2: {sum(e[0] for e in equations if evaluate(e[1:], e[0], concat=True))}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
