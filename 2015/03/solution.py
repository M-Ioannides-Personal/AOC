from icecream import ic

"""
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
"""

with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read()

current_position = (0, 0)
directions = {"^": (0, 1), "v": (0, -1), ">": (1, 0), "<": (-1, 0)}
all_visited = [current_position]
for direction in puzzle_input:
    dx, dy = directions[direction]
    current_position = (current_position[0] + dx, current_position[1] + dy)
    all_visited.append(current_position)

solution_1 = len(set(all_visited))
"""
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?
"""
santa_position = (0, 0)
robo_position = (0, 0)

all_visited = [santa_position]
for index, direction in enumerate(puzzle_input):
    dx, dy = directions[direction]
    if index % 2 == 0:
        santa_position = (santa_position[0] + dx, santa_position[1] + dy)
        all_visited.append(santa_position)
    else:
        robo_position = (robo_position[0] + dx, robo_position[1] + dy)
        all_visited.append(robo_position)

solution_2 = len(set(all_visited))


if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
