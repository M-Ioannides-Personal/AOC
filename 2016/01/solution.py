from icecream import ic

"""
Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

To what floor do the instructions take Santa?
"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read()

floor = 0
for instruction in puzzle_input:
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1
    else:
        ic("Something went wrong")
solution_1 = floor


"""
Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
"""

floor = 0
for position, instruction in enumerate(puzzle_input):
    if floor < 0:
        solution_2 = position
        break
    if instruction == "(":
        floor += 1
    elif instruction == ")":
        floor -= 1
    else:
        ic("Something went wrong")

if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 1: {solution_2}")
