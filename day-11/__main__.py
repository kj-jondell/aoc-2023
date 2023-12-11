from common import boilerplate
import os, logging, re, sys, math

part = int(os.environ.get('part', 1))

@boilerplate.part
def part1():
    height, width = 0, None
    galaxy_coords = []
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0:
            if not width:
                width = len(line)
            matches = re.finditer(r'#', line)
            for match in matches:
                x = match.start()
                #galaxy = match.group()
                logging.debug(f"{x,y} and {match.group()}")
                galaxy_coords.append((x,y))
            height += 1
    
    x_columns = set([x for x, y in galaxy_coords])
    y_rows = set([y for x, y in galaxy_coords])

    missing_columns = set(range(width)) - x_columns
    missing_rows = set(range(height)) - y_rows
    
    logging.debug(missing_columns)
    logging.debug(galaxy_coords)

    for index, (x, y) in enumerate(galaxy_coords):
        galaxy_coords[index] = (x+len([p for p in missing_columns if p < x]), y + len([p for p in missing_rows if p < y]))

    logging.debug(galaxy_coords)
    sum = 0
    for index, (x, y) in enumerate(galaxy_coords):
        for index_2, (x_2, y_2) in enumerate(galaxy_coords):
            if index < index_2:
                dist = abs(x_2 - x) + abs(y_2 - y) # since no diagonal movement is allowed we can simply get distance by horizontal shift and vertical shift
                logging.debug(f"Between galaxy {index+1} and galaxy {index_2+1}: {dist}")
                sum += dist

    logging.debug(f"width: {width} height: {height}. shortest between all pairs: {sum}")
    return sum

@boilerplate.part
def part2():
    height, width = 0, None
    galaxy_coords = []
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0:
            if not width:
                width = len(line)
            matches = re.finditer(r'#', line)
            for match in matches:
                x = match.start()
                #galaxy = match.group()
                logging.debug(f"{x,y} and {match.group()}")
                galaxy_coords.append((x,y))
            height += 1
    
    x_columns = set([x for x, y in galaxy_coords])
    y_rows = set([y for x, y in galaxy_coords])

    missing_columns = set(range(width)) - x_columns
    missing_rows = set(range(height)) - y_rows
    
    logging.debug(missing_columns)
    logging.debug(galaxy_coords)

    scaling_factor = 1_000_000 - 1 

    for index, (x, y) in enumerate(galaxy_coords):
        galaxy_coords[index] = (x+scaling_factor*len([p for p in missing_columns if p < x]), y + scaling_factor*len([p for p in missing_rows if p < y]))

    logging.debug(galaxy_coords)
    sum = 0
    for index, (x, y) in enumerate(galaxy_coords):
        for index_2, (x_2, y_2) in enumerate(galaxy_coords):
            if index < index_2:
                dist = abs(x_2 - x) + abs(y_2 - y) 
                logging.debug(f"Between galaxy {index+1} and galaxy {index_2+1}: {dist}")
                sum += dist

    logging.debug(f"width: {width} height: {height}. shortest between all pairs: {sum}")
    return sum


if part == 1:
    part1()
elif part == 2:
    part2()