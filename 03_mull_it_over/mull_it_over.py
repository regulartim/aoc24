import re
import time

begin = time.time()

###

PATTERN = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"


def execute_mul(mul: str) -> int:
    x, y = mul[4:-1].split(",")
    return int(x) * int(y)


with open("input.txt") as file:
    program = file.read().strip()

enabled = True
p1_sum, p2_sum = 0, 0
for instr in re.findall(PATTERN, program):
    match instr[:3]:
        case "mul":
            product = execute_mul(instr)
            p1_sum += product
            p2_sum += product * enabled
        case "do(":
            enabled = True
        case "don":
            enabled = False

print(f"Part 1: {p1_sum}")
print(f"Part 2: {p2_sum}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
