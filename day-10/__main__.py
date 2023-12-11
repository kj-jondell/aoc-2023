from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

directions = {'|' : '0110', '-' : '1001', 'L' : '0011', 'J': '1010', '7': '1100', 'F':'0101', 'S' : '1111', '.' : '0000'}

#def get_connections(pipe: str, pos: tuple, directions: str) -> tuple:
#    return None

direction_map = [(-1, 0), (0, 1), (0, -1), (1, 0)]

def get_loop(starting_pos: tuple, pipes: list, width: int, height: int) -> list:
    visited_pos = []
    no_more_options = False
    current_pos = starting_pos
    while not no_more_options:
        x, y = current_pos
        visited_pos.append(current_pos)
        current_pipe = pipes[y][x]
        for index, ch in enumerate(directions[current_pipe]):
            dx, dy = direction_map[index]
            logging.debug(f"{dx, dy} and {current_pos}")
            if int(ch) and x+dx in range(0, width) and y+dy in range(0, height) and (x+dx, y+dy) not in visited_pos:
                adjacent_pipe = pipes[dy+y][dx+x]
                logging.debug(f"current pipe {current_pipe} with pos {current_pos} adjacent to {adjacent_pipe} with pos {(dx+x,dy+y)}.")
                connecting_index = direction_map.index((dx*-1, dy*-1))
                if int(directions[adjacent_pipe][connecting_index]):
                    logging.debug(f"these pipes connect!, with index {index}")
                    current_pos = (dx+x, dy+y)
                    break
            if index == 3:
                no_more_options = True
    return visited_pos

@boilerplate.part
def part1():
    pipes = []
    current_pos = (0,0)
    width, height = 0, 0
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        pipes.append(['.' for _ in range(len(line))])
        if len(line)>0:
            matches = re.finditer(r'[\|\-LJ7FS]', line)
            for match in matches:
                x = match.start()
                pipe = match.group()
                logging.debug(f"pos: {(x,y)} and sign:{pipe}. Connects {directions[pipe]}")
                pipes[y][x] = pipe
                #if pipe == '7':
                #   current_pos = (x, y)
                if pipe == 'S':
                   current_pos = (x, y)
                   width = len(line)
    height = len(pipes)

    visited_pos = get_loop(current_pos, pipes, width, height)
    
    logging.debug(visited_pos)
    #for y in range(height):
    #    for x in range(width):
    #        if (x, y) not in visited_pos:
    #            print(".", end="")
    #        else:
    #            left_distance, right_distance = visited_pos.index((x,y)), len(visited_pos)-visited_pos.index((x,y))
    #            print(f"{min(left_distance, right_distance)}", end="")
    #    print()
    logging.debug(int(len(visited_pos)/2))
    return int(len(visited_pos)/2)

@boilerplate.part
def part2():
    pipes = []
    current_pos = (0,0)
    width, height = 0, 0
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        pipes.append(['.' for _ in range(len(line))])
        if len(line)>0:
            matches = re.finditer(r'[\|\-LJ7FS]', line)
            for match in matches:
                x = match.start()
                pipe = match.group()
                logging.debug(f"pos: {(x,y)} and sign:{pipe}. Connects {directions[pipe]}")
                pipes[y][x] = pipe
                if pipe == 'S':
                   current_pos = (x, y)
                   width = len(line)

    height = len(pipes)

    visited_pos = get_loop(current_pos, pipes, width, height)
    
    logging.debug(visited_pos)
    outer_pos, inner_pos = [], []
    for index, (x, y) in enumerate(visited_pos[:-1]):
        next_x, next_y = visited_pos[index+1] # next position
        #outer_x, outer_y = (y-dy, dx-x)
        #inner_x, inner_y = (dy-y, x-dx)
        outer_x, outer_y = (y-next_y, next_x-x) # check to the sides of moving direction
        inner_x, inner_y = (next_y-y, x-next_x) # check to the sides of moving direction

        if index > 0:
            prev_x, prev_y = visited_pos[index-1] # next position
            prev_outer_x, prev_outer_y = (prev_y-y, x-prev_x) # check to the sides of moving direction
            prev_inner_x, prev_inner_y = (y-prev_y, prev_x-x) # check to the sides of moving direction
            if (prev_outer_x, prev_outer_y) != (outer_x, outer_y): # if changing direction
                new_outer = x+prev_outer_x, y+prev_outer_y
                if new_outer not in visited_pos:
                    outer_pos.append(new_outer)
            if (prev_inner_x, prev_inner_y) != (inner_x, inner_y):
                new_inner = x+prev_inner_x, y+prev_inner_y
                if new_inner not in visited_pos:
                    inner_pos.append(new_inner)

        new_outer = x+outer_x, y+outer_y
        new_inner = x+inner_x, y+inner_y

        if new_outer not in visited_pos:
            outer_pos.append(new_outer)
        if new_inner not in visited_pos:
            inner_pos.append(new_inner)
    
    def complete_map(old_pos: tuple, pos_list: list):
        x, y = old_pos
        if x in range(0, width) and y in range(0, height):
            for dirx, diry in direction_map:
                if (dirx+x, diry+y) not in visited_pos and (dirx+x, diry+y) not in pos_list:
                    pos_list.append((dirx+x, diry+y))
                    complete_map((dirx+x, diry+y), pos_list)

    sys.setrecursionlimit(10000)
    for map in [outer_pos, inner_pos]:
        for point in map:
            complete_map(point, map)

    #missed_points = 0
    #for y in range(height):
    #    for x in range(width):
    #        if (x, y) in outer_pos:
    #            print("O", end="")
    #        elif (x, y) in inner_pos:
    #            print("I", end="")
    #        elif (x, y) not in visited_pos:
    #            print(".", end="")
    #            missed_points += 1
    #        else:
    #            left_distance, right_distance = visited_pos.index((x,y)), len(visited_pos)-visited_pos.index((x,y))
    #            print("X", end="")
    #    print()

    amt_inner_points = len(set(inner_pos).difference(set(visited_pos)))
    amt_outer_points = len(set(outer_pos).difference(set(visited_pos)))
    #print(amt_inner_points, amt_outer_points, missed_points)
    #return int(len(visited_pos)/2)
    return min(amt_inner_points, amt_outer_points)


if part == 1:
    part1()
elif part == 2:
    part2()