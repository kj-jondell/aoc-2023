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
    map, maps = [], []

    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            if len(seeds) == 0:
                seeds = [int(seed) for seed in re.findall(r'seeds: (.+)', line)[0].split()]
                logging.debug(line)
            elif len(re.findall(r'.+ map:', line)) > 0: #new map
                if len(map) > 0:
                    maps.append(map)
                    map = []
            else:
                map.append([int(num) for num in line.split()])
    
    maps.append(map)
    rev_maps = [sorted(map, key=lambda p: p[0]) for map in maps[::-1]]
    target, location = 0, 0
    keep_counting = True

    #logging.debug(f"map {rev_maps}")

    #def merge_maps(map_a, map_b):
    #    merged = sorted(map_a+map_b, key=lambda p: p[0]) 
    #    logging.debug(merged)
    #    for index, map in enumerate(merged[:-1]):
    #        next_dest_start, next_src_start, next_range_length = merged[index+1]
    #        dest_start, src_start, range_length = map
    #        if dest_start + range_length > next_dest_start:
    #            merged[index] = [dest_start, , next_dest_start-dest_start]
    #            print(dest_start, src_start, range_length)
    #                
    #        
    #    logging.debug(merged)

    #for index, map in enumerate(rev_maps[:-1]):
    #    merge_maps(map, rev_maps[index+1])

    #for map in rev_maps:
    #    for dest_start, src_start, range_length in map:
    #        if dest_start == src_start:
    #            logging.debug(f"{dest_start} {src_start} {range_length}")



    while keep_counting:
        for map in rev_maps:
            traversal = None
            for dest_start, src_start, range_length in map:
                if target in range(dest_start, dest_start+range_length):
                    traversal = src_start + target - dest_start 
                    break
            target = target if not traversal else traversal
            #logging.debug(f"{map} {target}")
        
        for index in range(0, len(seeds), 2):
            seed_start, seed_length = seeds[index], seeds[index+1]
            if target in range(seed_start, seed_start+seed_length):
                keep_counting = False
                break

        #logging.debug(target)
        if keep_counting:
            target = location + 1
            location += 1

    logging.debug(f"location {location} target {target}")
    return location 


if part == 1:
    part1()
elif part == 2:
    part2()