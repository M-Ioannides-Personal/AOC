import hashlib
from icecream import ic

"""
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
"""

input_key = "yzbqklnj"

for test_number in range(9999999):
    as_hash = hashlib.md5((input_key + str(test_number)).encode())
    if as_hash.hexdigest()[0:5] == "00000":
        solution_1 = test_number
        break

for test_number in range(9999999):
    as_hash = hashlib.md5((input_key + str(test_number)).encode())
    if as_hash.hexdigest()[0:6] == "000000":
        solution_2 = test_number
        break

if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
