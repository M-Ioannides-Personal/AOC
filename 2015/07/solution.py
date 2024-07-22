from icecream import ic

"""
Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

results_dictionary = {}


def binary_fun():
    while "a" not in results_dictionary.keys():
        for line in puzzle_input:
            orders = line.split(" -> ")
            inputs = orders[0].split(" ")
            output = orders[1]
            if len(inputs) == 1:
                try:
                    results_dictionary.setdefault(output, int(inputs[0]))
                except:
                    if inputs[0] in results_dictionary.keys():
                        results_dictionary[output] = results_dictionary[inputs[0]]
            elif "NOT" in inputs:
                if inputs[1] in results_dictionary.keys():
                    results_dictionary[output] = ~results_dictionary[inputs[1]] & 0xFFFF
            elif inputs[0] in results_dictionary.keys():
                if "LSHIFT" in inputs:
                    results_dictionary[output] = results_dictionary[inputs[0]] << int(
                        inputs[2]
                    )
                if "RSHIFT" in inputs:
                    results_dictionary[output] = results_dictionary[inputs[0]] >> int(
                        inputs[2]
                    )
                if inputs[2] in results_dictionary.keys():
                    if "AND" in inputs:
                        results_dictionary[output] = (
                            results_dictionary[inputs[0]]
                            & results_dictionary[inputs[2]]
                        )
                    if "OR" in inputs:
                        results_dictionary[output] = (
                            results_dictionary[inputs[0]]
                            | results_dictionary[inputs[2]]
                        )
            elif inputs[0].isdigit():
                if inputs[2] in results_dictionary.keys():
                    if "AND" in inputs:
                        results_dictionary[output] = (
                            int(inputs[0]) & results_dictionary[inputs[2]]
                        )
                    if "OR" in inputs:
                        results_dictionary[output] = (
                            int(inputs[0]) | results_dictionary[inputs[2]]
                        )


binary_fun()
solution_1 = results_dictionary["a"]

"""
The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?
"""

results_dictionary = {"b": solution_1}
binary_fun()
solution_2 = results_dictionary["a"]


if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
