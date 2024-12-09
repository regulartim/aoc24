import time

begin = time.time()

###


def create_disk_map(inp: str) -> list:
    result = []
    for idx, n in enumerate(inp):
        if int(n) == 0:
            continue
        if idx % 2 == 0:
            result.append((int(n), int(idx // 2)))
        else:
            result.append((int(n), None))
    return result


def to_blocks(disk: list) -> list:
    blocks = []
    for n, file_id in disk:
        blocks += [file_id] * int(n)
    return blocks


def left_fill(blocks: list) -> list:
    lptr, rptr = 0, len(blocks) - 1
    while lptr < rptr:
        if blocks[lptr] is not None:
            lptr += 1
            continue
        if blocks[rptr] is None:
            rptr -= 1
            continue
        blocks[lptr], blocks[rptr] = blocks[rptr], None
    return blocks


def defrag(disk: list) -> list:
    result = []
    moved = set()
    for idx, chunk in enumerate(disk):
        if chunk[1] is not None:
            if chunk not in moved:
                result.append(chunk)
                continue
            chunk = (chunk[0], None)
        while chunk[0] > 0:
            for other in reversed(disk[idx:]):
                if other[1] is None or other[0] > chunk[0] or other in moved:
                    continue
                result.append(other)
                moved.add(other)
                chunk = (chunk[0] - other[0], None)
                break
            else:
                result.append(chunk)
                break
    return result


def checksum(blocks: list) -> int:
    total = 0
    for idx, file_id in enumerate(blocks):
        if file_id is None:
            continue
        total += idx * file_id
    return total


with open("input.txt") as file:
    disk_map = create_disk_map(file.read().strip())

left_filled = left_fill(to_blocks(disk_map))
p2_filled = to_blocks(defrag(disk_map))

print(f"Part 1: {checksum(left_filled)}")
print(f"Part 2: {checksum(p2_filled)}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
