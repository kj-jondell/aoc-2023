from common import boilerplate
import os, logging, re, sys, math
import itertools

part = int(os.environ.get('part', 1))

def valid_string(pipes: str, groups: list):
    return [len(gr) for gr in re.findall(r'[(#)]+', pipes)] == groups

@boilerplate.part
def part1():
    p_sum = 0
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            conditions = re.findall(r'[.]+|[(#)]+|[(?)]+', line)
            all_unknowns = [match.start() for match in re.finditer(r'[(?)]', line)]
            digits = [int(digit) for digit in re.findall(r'(\d+)', line)]

            amt_unknowns, amt_known_broken = line.count("?"), line.count("#")
            amt_unknown_operational = amt_unknowns + amt_known_broken - sum(digits)

            arrangements = 0
            for combo in itertools.combinations(all_unknowns, amt_unknown_operational):
                if valid_string("".join(["." if index in combo else "#" if ch != "." else "." for index, ch in enumerate("".join(conditions))]), digits):
                    arrangements += 1
            
            logging.debug("".join(conditions))
            logging.debug(arrangements)

            p_sum += arrangements

    return p_sum

@boilerplate.part
def part2():
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            pass

if part == 1:
    part1()
elif part == 2:
    part2()