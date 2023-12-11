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

    new_format = [[[src_start, src_start+length-1, dest_start-src_start] for dest_start, src_start, length in map] for map in maps]

    def merge_maps(map_a, map_b):
        unmerged_maps = sorted(map_a+map_b)        
        #for index, map in enumerate(unmerged_maps[:-1]):
        #logging.debug(sorted(map_a))
        #logging.debug(sorted(map_b))
        #logging.debug(unmerged_maps)
        index = 0
        while index<len(unmerged_maps)-1:
            src_start, src_end, diff = unmerged_maps[index]
            next_src_start, next_src_end, next_diff = unmerged_maps[index+1]
            if src_start == next_src_start: #enclosed
                new_src_start, new_src_end, new_diff = next_src_start, src_end, diff+next_diff
                unmerged_maps[index][2] = new_diff
                unmerged_maps[index+1][0] = src_end + 1
                unmerged_maps.insert(index, [new_src_start, new_src_end, new_diff])
                unmerged_maps[index:] = sorted(unmerged_maps[index:])
                #logging.debug(unmerged_maps)
                #logging.debug(index)
                #logging.debug("---")
            elif src_start >= next_src_start and src_end <= next_src_end: #enclosed
                new_src_start, new_src_end, new_diff = next_src_start, src_end, diff+next_diff
                unmerged_maps[index][2] = new_diff
                unmerged_maps[index+1][0] = src_end + 1
                #unmerged_maps.insert(index+1, [new_src_start, new_src_end, new_diff])
                unmerged_maps[index:] = sorted(unmerged_maps[index:])
                #logging.debug(unmerged_maps)
                #logging.debug(index)
                #logging.debug("---")
            elif next_src_start <= src_end: #overlapping
                new_src_start, new_src_end, new_diff = next_src_start, min(src_end, next_src_end), diff+next_diff
                unmerged_maps[index][1] = new_src_start - 1
                unmerged_maps[index+1][0] = src_end + 1
                unmerged_maps[index+1][1] = max(src_end + 1, next_src_end)
                unmerged_maps.insert(index+1, [new_src_start, new_src_end, new_diff])
                unmerged_maps[index:] = sorted(unmerged_maps[index:])
                #logging.debug(unmerged_maps)
                #logging.debug(index)
                #logging.debug("---")
            index += 1
        unmerged_maps.sort()
        return unmerged_maps

    while len(new_format) > 1:
    #for _ in range(2):
        new_format[0] = merge_maps(new_format[0], new_format[1])
        new_format.remove(new_format[1])
    new_format = new_format[0]
    logging.debug(new_format)

    # dest_start, src_start, length = 
    # (dest_start, src_start, length) => (src_start, src_end, diff)

    return 0


if part == 1:
    part1()
elif part == 2:
    part2()