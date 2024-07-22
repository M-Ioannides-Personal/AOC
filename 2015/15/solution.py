from icecream import ic
from typing import List

"""
Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything but calories.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

ingredient_statistics = {}
for ingredient in puzzle_input:
    name, stats = ingredient.split(":")
    ingredient_statistics[name] = [
        int(stat.split(" ")[-1]) for stat in stats.split(", ")
    ]

def combinations_sum_100():
    result = []
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                result.append([a, b, c, d])
    return result

all_combos = combinations_sum_100()

def calculate_final_score(ingredient_statistics: dict, ingredient_weights: List[int]):
    weighted_stats = []
    for stats, weight in zip(ingredient_statistics.values(), ingredient_weights):
        weighted_stats.append([stat * weight for stat in stats[:-1]])

    summed_statistic_scores = [sum(stat_scores) for stat_scores in zip(*weighted_stats)]
    
    final_score = 1
    for specific_statistic_score in summed_statistic_scores:
        score = max(specific_statistic_score, 0)
        final_score *= score

    return final_score


solution_1 = 0
for combo in all_combos:
    solution_1 = max(
        calculate_final_score(
            ingredient_statistics=ingredient_statistics, ingredient_weights=combo
        ),
        solution_1,
    )

"""
Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system)
"""


def calculate_final_score_cal(ingredient_statistics: dict, ingredient_weights: List[int]):
    weighted_stats = []
    for stats, weight in zip(ingredient_statistics.values(), ingredient_weights):
        weighted_stats.append(stats[-1] * weight)
    callories = sum(weighted_stats)
    if callories != 500:
        return -999

    weighted_stats = []
    for stats, weight in zip(ingredient_statistics.values(), ingredient_weights):
        weighted_stats.append([stat * weight for stat in stats[:-1]])

    summed_statistic_scores = [sum(stat_scores) for stat_scores in zip(*weighted_stats)]
    
    final_score = 1
    for specific_statistic_score in summed_statistic_scores:
        score = max(specific_statistic_score, 0)
        final_score *= score

    return final_score


solution_2 = 0
for combo in all_combos:
    solution_2 = max(
        calculate_final_score_cal(
            ingredient_statistics=ingredient_statistics, ingredient_weights=combo
        ),
        solution_2,
    )


if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
