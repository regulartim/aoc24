import time

begin = time.time()

###


def evaluate(out: str, gates: dict) -> int:
    gate = gates[out]
    if isinstance(gate, int):
        return gate
    match gate.split():
        case a, "AND", b:
            return int(evaluate(a, gates) and evaluate(b, gates))
        case a, "OR", b:
            return int(evaluate(a, gates) or evaluate(b, gates))
        case a, "XOR", b:
            return int(evaluate(a, gates) != evaluate(b, gates))


def simulate(gates: dict) -> int:
    z_gates = [gate for gate in gates if gate.startswith("z")]
    result = 0
    for idx, gate in enumerate(sorted(z_gates)):
        result += evaluate(gate, gates) * 2**idx
    return result


def find_swaps(gates: dict) -> dict:
    or_gates, inp_xors, carry_xors, and_gates, invalid = {}, {}, {}, {}, {}
    gates = [(out, gate) for out, gate in gates.items() if not isinstance(gate, int)]
    or_gates = [(out, gate) for out, gate in gates if " OR" in gate]
    and_gates = [(out, gate) for out, gate in gates if " AND" in gate]
    inp_xors = [(out, gate) for out, gate in gates if " XOR" in gate and "x" in gate and "y" in gate and out[0] != "z"]
    carry_xors = [(out, gate) for out, gate in gates if " XOR" in gate and "x" not in gate and "y" not in gate]

    for out, gate in or_gates:
        if "x" in gate or "y" in gate or out[0] == "z":
            invalid[out] = gate

    for out, gate in carry_xors:
        if out[0] != "z":
            invalid[out] = gate

    for out, gate in inp_xors:
        for _, other in carry_xors:  # .values():
            if out in other:
                break
        else:
            invalid[out] = gate

    for out, gate in and_gates:
        if out[0] == "z":
            invalid[out] = gate
        for _, other in or_gates:
            if out in other:
                break
        else:
            invalid[out] = gate

    first_gate = next(out for out, gate in gates if "x00" in gate)
    last_gate = max(gates)[0]
    del invalid[first_gate]
    del invalid[last_gate]
    return invalid


with open("input.txt") as file:
    sections = file.read().split("\n\n")

logic_gates = {}
for line in sections[0].splitlines():
    wire, val = line.strip().split(": ")
    logic_gates[wire] = int(val)
for line in sections[1].splitlines():
    g, output = line.strip().split(" -> ")
    logic_gates[output] = g

print(f"Part 1: {simulate(logic_gates)}")
print(f"Part 2: {", ".join(sorted(find_swaps(logic_gates)))}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
