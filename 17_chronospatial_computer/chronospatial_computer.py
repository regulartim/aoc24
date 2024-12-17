import re
import time

begin = time.time()

###


def execute(prog: list, registers: list) -> list:
    combo = lambda o: o if o < 4 else registers[o - 4]
    pointer = 0
    result = []
    while pointer < len(prog):
        opcode, operand = prog[pointer], prog[pointer + 1]
        match opcode:
            case 0:
                registers[0] = registers[0] // (2 ** combo(operand))
            case 1:
                registers[1] = registers[1] ^ operand
            case 2:
                registers[1] = combo(operand) % 8
            case 3:
                if registers[0] != 0:
                    pointer = operand
                    continue
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                result.append(combo(operand) % 8)
            case 6:
                registers[1] = registers[0] // (2 ** combo(operand))
            case 7:
                registers[2] = registers[0] // (2 ** combo(operand))
        pointer += 2
    return result


def find_register_value(prog: list, pointer: int, value: int) -> int:
    if -pointer > len(program):
        return value
    exponent = len(prog) + pointer
    for n in range(8):
        test_value = value + n * (8**exponent)
        output = execute(program, [test_value, 0, 0])
        if len(output) <= pointer:
            continue
        if output[pointer] == program[pointer]:
            result = find_register_value(prog, pointer - 1, value + n * (8**exponent))
            if result is None:
                continue
            return result
    return None


with open("input.txt") as file:
    a, b, c, *program = map(int, re.findall(r"\d+", file.read()))

print(f"Part 1: {execute(program, [a, b, c])}")
print(f"Part 2: {find_register_value(program, -1, 0)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
