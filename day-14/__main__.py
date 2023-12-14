from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

@boilerplate.part
def part1():

    sum = 0
    rocks = {}

    width, height = None, 0

    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0: # read in data
            height += 1
            if not width:
                width = len(line)
            matches = re.finditer(r'([O#])', line)
            for match in matches:
                x = match.start()
                stationary = match.group() == "#"
                logging.debug(f"Adding {x,y}, a {'stationary' if stationary else 'moving'} rock")
                rocks[(x,y)] = stationary
    
    # MOVE ALL ROCKS UP
    for _ in range(height): # iterate height times since cannot move furter up
        for y in range(height):
            for x in range(width):
                dx, dy = x, y - 1
                if dx in range(width) and dy in range(height):
                    if (x, y) in rocks.keys() and not rocks[(x, y)] and (dx, dy) not in rocks.keys():
                        rocks[(dx, dy)] = rocks[(x,y)]
                        rocks.pop((x,y))

    for y in range(height):
        amt_moving = 0
        for x in range(width):
            sign = "."
            if (x, y) in rocks.keys():
                if rocks[(x, y)]:
                    sign = "#" 
                else:
                    sign = "O" 
                    amt_moving += 1
        #    print(sign, end = "")   
        #print(f" {height - y}", amt_moving, amt_moving * (height - y))
        sum += amt_moving * (height - y)

    return sum

@boilerplate.part
def part2():
    sum = 0
    rocks = {}

    width, height = None, 0

    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0: # read in data
            height += 1
            if not width:
                width = len(line)
            matches = re.finditer(r'([O#])', line)
            for match in matches:
                x = match.start()
                stationary = match.group() == "#"
                logging.debug(f"Adding {x,y}, a {'stationary' if stationary else 'moving'} rock")
                rocks[(x,y)] = stationary
    
    ## automatically identify pattern! |-----|(p,q)..(p,q) 
    # MOVE ALL ROCKS UP
    for cycle in range(45):
        #prev_rocks = rocks.copy()
        for ddx, ddy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            for _ in range(height if ddy != 0 else width): # iterate height times since cannot move furter up
                for y in range(height):
                    for x in range(width):
                        dx, dy = x+ddx, y+ddy
                        if dx in range(width) and dy in range(height):
                            if (x, y) in rocks.keys() and not rocks[(x, y)] and (dx, dy) not in rocks.keys():
                                rocks[(dx, dy)] = rocks[(x,y)]
                                rocks.pop((x,y))
        #if prev_rocks == rocks:
        #    logging.debug(cycle)

        sum = 0
        for y in range(height):
            amt_moving = 0
            for x in range(width):
                sign = "."
                if (x, y) in rocks.keys():
                    if rocks[(x, y)]:
                        sign = "#" 
                    else:
                        sign = "O" 
                        amt_moving += 1
            #    print(sign, end = "")   
            #print(f" {height - y}", amt_moving, amt_moving * (height - y))
            sum += amt_moving * (height - y)
        #if sum == 64:
        logging.debug(f"cycle: {cycle} and sum {sum}")

    return sum


if part == 1:
    part1()
elif part == 2:
    part2()