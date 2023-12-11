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
                   width = len()
    
    x, y = current_pos
    current_pipe = pipes[y][x]
    for index, ch in enumerate(directions[current_pipe]):
        dx, dy = direction_map[index]
        if int(ch) and x+dx in range(0, ):
            adjacent_pipe = pipes[dy+y][dx+x]
            logging.debug(f"current pipe {current_pipe} with pos {current_pos} adjacent to {adjacent_pipe} with pos {(dx+x,dy+y)}.")
            if int(f"0x{directions[current_pipe]}", 0) & int(f"0x{directions[adjacent_pipe]}", 0):
                logging.debug(f"these pipes connect!")
        

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