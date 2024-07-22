from icecream import ic

"""
Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.
Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""
with open("input.txt", "r") as open_file:
    puzzle_input = open_file.read().splitlines()

distance_dictionary = {}
def distance_travelled(line:str, time:int):
    name, speed, duration, rest = line.split(' ')[0], int(line.split(' ')[3]), int(line.split(' ')[6]), int(line.split(' ')[13])
    distance = 0
    state = 'f'
    state_time = 0
    for _ in range(time):
        if state == 'f':
            distance += speed
            state_time += 1
            if state_time == duration:
                state = 'r'
                state_time = 0
        elif state == 'r':
            state_time += 1
            if state_time == rest:
                state = 'f'
                state_time = 0
    distance_dictionary[name]= distance


for reindeer in puzzle_input:
    distance_travelled(reindeer, time=2503)

solution_1 = max(distance_dictionary.values())

"""
Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
"""
reindeer_stats = {}
for reindeer in puzzle_input:
    name, speed, duration, rest = reindeer.split(' ')[0], int(reindeer.split(' ')[3]), int(reindeer.split(' ')[6]), int(reindeer.split(' ')[13])
    reindeer_stats[name] = [speed, duration, rest]

def lead_points_scored(time:int):
    reindeer_competitors = {key: {'distance':0, 'state':'f', 'state_time':0, 'points':0} for key in reindeer_stats.keys()}

    for _ in range(time):
        distance_to_beat = -1
        leaders = []

        for reindeer, scores in reindeer_competitors.items():
            speed, duration, rest = reindeer_stats[reindeer]
            if scores['state'] == 'f':
                scores['distance'] += speed
                scores['state_time'] += 1
                if scores['state_time'] == duration:
                    scores['state'] = 'r'
                    scores['state_time'] = 0

            elif scores['state'] == 'r':
                scores['state_time'] += 1
                if scores['state_time'] == rest:
                    scores['state'] = 'f'
                    scores['state_time'] = 0
            
            if scores['distance'] > distance_to_beat:
                distance_to_beat = scores['distance']
                leaders = [reindeer]
            elif scores['distance'] == distance_to_beat:
                leaders.append(reindeer)

        for individual in leaders:
            reindeer_competitors[individual]['points'] += 1

    return max(stats['points'] for stats in reindeer_competitors.values())
    
solution_2 = lead_points_scored(time=2503)


if __name__ == "__main__":
    ic(f"Part 1: {solution_1}")
    ic(f"Part 2: {solution_2}")
