from icecream import ic

"""
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

How many strings are nice?

"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

naughty_combo = ["ab", "cd", "pq", "xy"]
vowels = ["a", "e", "i", "o", "u"]


def nice_test(test_string: str) -> bool:
    if any(combo in test_string for combo in naughty_combo):
        return False
    if sum(test_string.count(vowel) for vowel in vowels) < 3:
        return False
    if any(a == b for a, b in zip(test_string, test_string[1:])):
        return True
    return False


solution_1 = 0
for line in puzzle_input:
    solution_1 += nice_test(line)

"""
It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""


def new_nice_test(test_string: str) -> bool:
    if all(
        test_string.count(test_string[i : i + 2]) < 2
        for i in range(len(test_string) - 1)
    ):
        return False
    if all(a != b for a, b in zip(test_string, test_string[2:])):
        return False
    return True


solution_2 = 0
for line in puzzle_input:
    solution_2 += new_nice_test(line)

if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
