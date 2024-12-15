import time

begin = time.time()

###

DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def add_tuples(a: tuple, b: tuple) -> tuple:
    return tuple(map(sum, zip(a, b)))


def is_movable(left_part: tuple, right_part: tuple, direction:str, warehouse:dict) -> bool:
    left_next = add_tuples(left_part, DIRECTIONS[direction])
    right_next = add_tuples(right_part, DIRECTIONS[direction])
    match warehouse[left_next] + warehouse[right_next]:
        case "..":
            return True
        case "[]":
            return is_movable(left_next, right_next, direction, warehouse)
        case "].":
            return is_movable(add_tuples(left_next, (-1,0)), left_next, direction, warehouse)
        case ".[":
            return is_movable(right_next, add_tuples(right_next, (1,0)), direction, warehouse)
        case "][":
            return is_movable(add_tuples(left_next, (-1,0)), left_next, direction, warehouse) \
                and is_movable(right_next, add_tuples(right_next, (1,0)), direction, warehouse)
    return False


def move(postition: tuple, direction: str, warehouse: dict) -> tuple:
    next_pos = add_tuples(postition, DIRECTIONS[direction])
    next_char = warehouse[next_pos]
    if next_char == "#":
        return postition
    if next_char == "O" or next_char in "[]" and direction in "<>":
        result = move(next_pos, direction, warehouse)
        if result == next_pos:
            return postition
    if next_char in "[]" and direction in "^v":
        if next_char == "[":
            other_pos = add_tuples(next_pos, (1,0))
            args = (next_pos, other_pos, direction, warehouse)
        else:
            other_pos = add_tuples(next_pos, (-1,0))
            args = (other_pos, next_pos, direction, warehouse)
        if not is_movable(*args):
            return postition
        move(next_pos, direction, warehouse)
        move(other_pos, direction, warehouse)
    warehouse[postition], warehouse[next_pos] = warehouse[next_pos], warehouse[postition]
    return next_pos


def execute(movements: str, bot_pos: tuple, warehouse: dict) -> dict:
    for m in movements:
        bot_pos = move(bot_pos, m, warehouse)
    return warehouse


warehouse_map, second_warehouse_map = {}, {}
robot_position = (0,0)
with open("input.txt") as file:
    sections = file.read().split("\n\n")
    for y, line in enumerate(sections[0].split()):
        for x, char in enumerate(line):
            warehouse_map[(x, y)] = char
            second_warehouse_map[(2*x, y)] = char
            second_warehouse_map[(2*x+1, y)] = char
            if char == "O":
                second_warehouse_map[(2*x, y)] = "["
                second_warehouse_map[(2*x+1, y)] = "]"
            if char == "@":
                robot_position = (x, y)
                second_warehouse_map[(2*x+1, y)] = "."
    robot_movements = "".join(sections[1].split())

second_robot_position = (2*robot_position[0], robot_position[1])
execute(robot_movements, robot_position, warehouse_map)
execute(robot_movements, second_robot_position, second_warehouse_map)

print(f"Part 1: {sum(p[0] + 100 *p[1]for p, char in warehouse_map.items() if char == "O")}")
print(f"Part 2: {sum(p[0] + 100 *p[1]for p, char in second_warehouse_map.items() if char == "[")}")

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
