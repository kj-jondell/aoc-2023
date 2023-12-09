from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

@boilerplate.part
def part1():
    nodes = {}
    lr_instructions = None
    start, end = 'AAA', 'ZZZ'

    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            if not lr_instructions:
                match = re.findall(r'([RL])', line)
                if len(match) > 0:
                    lr_instructions = match
            
            mapping = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})', line)
            for matches in mapping:
                label, left, right = matches
                nodes[label] = {"L":left, "R":right}

    current_node = start
    amt_steps = 1
    while current_node != end:
        for instruction in lr_instructions:
            current_node = nodes[current_node][instruction]
            if current_node == end:
                break
            amt_steps += 1

    logging.debug(f"node {current_node} in {amt_steps} steps")
    return amt_steps

@boilerplate.part
def part2():
    nodes = {}
    lr_instructions = None

    start_key, end_key = r'(\w{2}A)', r'(\w{2}Z)'

    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            if not lr_instructions:
                match = re.findall(r'([RL])', line)
                if len(match) > 0:
                    lr_instructions = match
            
            mapping = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})', line)
            for matches in mapping:
                label, left, right = matches
                #nodes[label] = (left, right)
                nodes[label] = {"L":left, "R":right}

    start_keys = set(re.findall(start_key, " ".join(nodes.keys())))
    end_keys = set(re.findall(end_key, " ".join(nodes.keys())))

    # 1. Find repetitions
    current_node = next(iter(start_keys))

    prod_set = {1}
    #logging.debug("Doing start keys")
    #for set_keys in [start_keys, end_keys]:
    #    for start in set_keys:
    for start in start_keys:
        current_node = start
        amt_steps = 1
        while current_node not in start_keys.union(end_keys) or amt_steps == 1:
            for instruction in lr_instructions:
                current_node = nodes[current_node][instruction]
                if current_node in end_keys:
                    break
                amt_steps += 1
        logging.debug(f"{start}=>{current_node} takes {amt_steps} steps")
        #prod_sum *= amt_steps
        logging.debug(f"steps/instructions is: {(amt_steps)/len(lr_instructions)}")

        prod_set = prod_set.union(set([n for n in range(1, amt_steps) if amt_steps % n == 0]))
        
    #   logging.debug("Doing end keys")
    logging.debug(prod_set)
    prod_sum = 1
    for factor in prod_set:
        prod_sum *= factor

    return prod_sum


if part == 1:
    part1()
elif part == 2:
    part2()