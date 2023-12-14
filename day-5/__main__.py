from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

def merge_seeds(seeds: list, map: list) -> list:
    initial_seeds = seeds[:]
    for row in map:
        dest_start, src_start, range_length = row
        for index, seed in enumerate(initial_seeds):
            if seed in range(src_start, src_start+range_length):
                seeds[index] = dest_start + seed - src_start 
    return seeds

@boilerplate.part
def part1():
    seeds = []
    map = []

    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            if len(seeds) == 0:
                seeds = [int(seed) for seed in re.findall(r'seeds: (.+)', line)[0].split()]
                logging.debug(line)
            elif len(re.findall(r'.+ map:', line)) > 0: #new map
                if len(map) > 0:
                    seeds = merge_seeds(seeds, map)
                    map = []
                    logging.debug(f"{line} {seeds}")
            else:
                map.append([int(num) for num in line.split()])
    
    if len(map) > 0:
        seeds = merge_seeds(seeds, map)

    logging.debug(f"result: {seeds}")
    logging.debug(f"min: {min(seeds)}")
    return min(seeds)

@boilerplate.part
def part2():
    seeds = []
    map_list, maps = [], []

    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            if len(seeds) == 0:
                seeds = [int(seed) for seed in re.findall(r'seeds: (.+)', line)[0].split()]
                logging.debug(line)
            elif len(re.findall(r'.+ map:', line)) > 0: #new map
                if len(map_list) > 0:
                    maps.append(map_list)
                    map_list = []
            else:
                map_list.append([int(num) for num in line.split()])
    
    maps.append(map_list)

    ### 

    reverse_list = [map for map in maps[::-1]]

    logging.debug(reverse_list)

    return 0


if part == 1:
    part1()
elif part == 2:
    part2()