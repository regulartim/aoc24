import re
import time

begin = time.time()

###

X_DIM, Y_DIM = 101, 103


def position_after(seconds: int, robot: tuple) -> tuple:
    px, py, vx, vy = robot
    px = (px + vx * seconds) % X_DIM
    py = (py + vy * seconds) % Y_DIM
    return px, py


def safety_factor(positions: list) -> int:
    upper_left = sum(p[0] < X_DIM // 2 and p[1] < Y_DIM // 2 for p in positions)
    upper_right = sum(p[0] > X_DIM // 2 and p[1] < Y_DIM // 2 for p in positions)
    lower_left = sum(p[0] < X_DIM // 2 and p[1] > Y_DIM // 2 for p in positions)
    lower_right = sum(p[0] > X_DIM // 2 and p[1] > Y_DIM // 2 for p in positions)
    return upper_left * upper_right * lower_left * lower_right


def christmas_tree_detector(bots: list) -> int:
    seconds = 0
    while True:
        seconds += 1
        positions = [position_after(seconds, bot) for bot in bots]
        if len(positions) == len(set(positions)):
            return seconds


def print_positions(positions: list) -> str:
    positions = set(positions)
    result = ""
    for y in range(Y_DIM):
        for x in range(X_DIM):
            if (x, y) in positions:
                result += "#"
            else:
                result += "."
        result += "\n"
    return result


with open("input.txt") as file:
    robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in file]

final_positions = [position_after(100, bot) for bot in robots]
tree_seconds = christmas_tree_detector(robots)
tree = print_positions([position_after(tree_seconds, bot) for bot in robots])

print(f"Part 1: {safety_factor(final_positions)}")
print(f"Part 2: {tree_seconds}")
# print(tree)

###

end = time.time()
runtime_in_ms = round((end - begin) * 1000, 3)
print(f"Runtime: {runtime_in_ms:.3f} ms")
