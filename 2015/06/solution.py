from icecream import ic

"""
Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

After following the instructions, how many lights are lit?

"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

grid = []
for _ in range(1000):
    grid.append([0] * 1000)


def light_changes(line: str):
    x1, y1 = line.split(" ")[-3].split(",")
    x2, y2 = line.split(" ")[-1].split(",")
    for y in range(int(y1), int(y2) + 1):
        for x in range(int(x1), int(x2) + 1):
            if "turn on" in line:
                grid[x][y] = 1
            elif "turn off" in line:
                grid[x][y] = 0
            else:
                grid[x][y] = (grid[x][y] - 1) ** 2


for input_line in puzzle_input:
    light_changes(input_line)

solution_1 = 0
for row in grid:
    solution_1 += row.count(1)

"""
The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?
"""
grid = []
for _ in range(1000):
    grid.append([0] * 1000)


def elfish_light_changes(line: str):
    x1, y1 = line.split(" ")[-3].split(",")
    x2, y2 = line.split(" ")[-1].split(",")
    for y in range(int(y1), int(y2) + 1):
        for x in range(int(x1), int(x2) + 1):
            if "turn on" in line:
                grid[x][y] += 1
            elif "turn off" in line:
                grid[x][y] -= 1
                if grid[x][y] < 0:
                    grid[x][y] = 0
            else:
                grid[x][y] += 2


solution_2 = 0
for input_line in puzzle_input:
    elfish_light_changes(input_line)

for row in grid:
    solution_2 += sum(row)

if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
