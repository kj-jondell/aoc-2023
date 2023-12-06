from common import boilerplate
import os, logging, re, sys, math

part = int(os.environ.get('part', 1))

def quadratic_formula(p: float, q: float):
    part = math.sqrt(-4*q+p**2)
    first = -p/2
    return first+part, first-part

def get_distances(amt_time: int, min_distance: int) -> "list[int]":
    # running_time * velocity
    distances = []
    for holding_time in range(amt_time):
        distance = (amt_time-holding_time) * (holding_time)
        if distance > min_distance:
            distances.append(distance)
    return distances

@boilerplate.part
def part1():
    times, distances = [], []
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            for matches in re.findall(r'Time: (.+)', line):
                times = [int(match) for match in matches.split()]
            for matches in re.findall(r'Distance: (.+)', line):
                distances = [int(match) for match in matches.split()]

    prod_sum = 1
    for index, time in enumerate(times):
        #prod_sum *= len(get_distances(time, distances[index]))
        logging.debug(f"amt_time: {time} distance: {distances[index]} and roots: {quadratic_formula(time, distances[index])} and solution: {len(get_distances(time, distances[index]))}")

    return prod_sum

@boilerplate.part
def part2():
    time, distance = 0, 0
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            for matches in re.findall(r'Time: (.+)', line):
                time = int("".join(matches.split()))
            for matches in re.findall(r'Distance: (.+)', line):
                distance = int("".join(matches.split()))


    prod_sum = len(get_distances(time, distance))
    logging.debug(prod_sum)

    return prod_sum

if part == 1:
   part1()
elif part == 2:
   part2()