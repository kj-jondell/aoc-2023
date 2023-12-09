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
    
    rev_maps = [sorted(map) for map in maps[::-1]]
    #rev_maps.sort(key=lambda p: (p[0], p[2]))
    #logging.debug(rev_maps)

    names = ["Seed", "location"][::-1]

    def merge_maps(map_a, map_b):
        range_a = set(range(map_a[0], map_a[0]+map_a[2]))
        range_b = set(range(map_b[0], map_b[0]+map_b[2]))
        diff_a = range_a.difference(range_b)
        union = range_a.union(range_b)
        diff_b = range_b.difference(range_a)
        unity_map = [[min(diff_a), map_a[1], max(diff_a)] if diff_a else None,[min(union), map_b[1]-map_a[1], max(union)] if union else None, [min(diff_b), map_b[1], max(diff_b)] if diff_b else None]
        return unity_map

    rev_maps[0] = sorted(rev_maps[0]+rev_maps[1])
    rev_maps.remove(rev_maps[1])
    for index, map in enumerate(rev_maps[0][:-1]):
        map = merge_maps(map, rev_maps[0][index+1])
        logging.debug(map)

    lowest_seed, lowest_location = None, None
    #test_nums = []
    #for ranges in rev_maps[0]:
    #    dest_start, src_start, length = ranges
    #    test_nums.append(dest_start)

    for test_num in [0]:
        curr_num = test_num
        for index, map in enumerate(rev_maps):
            logging.debug(f"{map} is")



            #logging.debug(f"New map ({names[index].lower()}=>{names[index+1].lower()}), printing ranges:\ntest_num is {curr_num}")
            #found_num = False
            #for ranges in map:
            #dest_start, src_start, length = map
            #logging.debug(f"dest_start: {dest_start:>10}, src_start: {src_start:>10}, length: {length}")
            #if curr_num in range(dest_start, dest_start+length) and not found_num:
            #    logging.debug(f"{curr_num}=>{curr_num+src_start-dest_start}")
            #    curr_num += src_start-dest_start
            #    found_num = True

    

    ##other_format = [for map in rev_maps]
    #rev_maps[0:1] = [rev_maps[0]+rev_maps[1]]
    #rev_maps = [sorted(map, key=lambda p: p[0]) for map in rev_maps]

    #for index, map in enumerate(rev_maps[0][:-1]):
    #    dest_start, src_start, length = map
    #    dest_end = dest_start + length - 1
    #    src_end = src_start + length - 1
    #    diff = src_end-dest_end
    #    next_dest_start, next_src_start, next_length = rev_maps[0][index+1]
    #    next_dest_end = next_dest_start + next_length - 1
    #    next_src_end = next_src_start + next_length - 1
    #    next_diff = next_src_end-next_dest_end
    #    if 


    #logging.debug("-----")
    #for map_list in rev_maps:
    #    for current_range in map_list:
    #        dest_start, src_start, length = current_range
    #        dest_end = dest_start + length - 1
    #        src_end = src_start + length - 1
    #        diff = src_end-dest_end
    #        logging.debug(f"({dest_start}-{dest_end})=>({src_start}-{src_end}) : {length} {'+' if diff>0 else ''}{diff}")

    #    logging.debug("-----")

    #return location 
    return lowest_location


if part == 1:
    part1()
elif part == 2:
    part2()