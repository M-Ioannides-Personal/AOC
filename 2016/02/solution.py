from icecream import ic

"""
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.
"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

total_paper = 0
for instruction in puzzle_input:
    height, width, length = map(int, instruction.split("x"))
    box = 2 * length * width + 2 * width * height + 2 * height * length
    stats = [height, width, length]
    stats.sort()
    slack = stats[0] * stats[1]
    total_paper += box + slack


solution_1 = total_paper
"""
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
"""
total_ribbon = 0
for instruction in puzzle_input:
    height, width, length = map(int, instruction.split("x"))
    bow = length * width * height
    stats = [height, width, length]
    stats.sort()
    perimeter = stats[0] + stats[1] + stats[0] + stats[1]
    total_ribbon += perimeter + bow


solution_2 = total_ribbon

if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
