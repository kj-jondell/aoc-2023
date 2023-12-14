from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

def get_reflection_points(line: str):
    reflection_points = []

    for reflection_point in range(1,len(line)):
        original_line = line[0:reflection_point]
        reflected_line = line[reflection_point:]
        if len(original_line) < len(reflected_line):
            reflected_line = reflected_line[:len(original_line)]
        elif len(original_line) > len(reflected_line):
            original_line = original_line[len(original_line)-len(reflected_line):]
        if original_line == reflected_line[::-1]:
            reflection_points.append(reflection_point)
    return reflection_points

@boilerplate.part
def part1():
    lines, list_of_lines = [], []
    
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            lines.append(line)
        else:
            list_of_lines.append(lines)
            vertical_lines = []  
            for index in range(len(lines[0])): # vertical search
                new_line = "".join([line[index] for line in lines])
                vertical_lines.append(new_line)
            list_of_lines.append(vertical_lines)
            lines = []  

    sum = 0

    for index, lines in enumerate(list_of_lines):
        reflection_points = []
        for line in lines: 
            line_reflection_points = get_reflection_points(line)
            if not reflection_points:
                reflection_points += line_reflection_points
            else:
                reflection_points = list(set(line_reflection_points).intersection(set(reflection_points)))
                if not reflection_points:
                    break
        if reflection_points:
            sum += reflection_points[0] * (1 if index % 2 == 0 else 100)
        logging.debug(reflection_points)

    return sum

@boilerplate.part
def part2():
    lines, list_of_lines = [], []
    
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            lines.append(line)
        else:
            list_of_lines.append(lines)
            vertical_lines = []  
            for index in range(len(lines[0])): # vertical search
                new_line = "".join([line[index] for line in lines])
                vertical_lines.append(new_line)
            list_of_lines.append(vertical_lines)
            lines = []  

    sum = 0

    for index, lines in enumerate(list_of_lines):
        reflection_points = {}
        for line in lines: 
            for reflection_point in get_reflection_points(line):
                if reflection_point in reflection_points.keys():
                    reflection_points[reflection_point] += 1
                else:
                    reflection_points[reflection_point] = 1
        #logging.debug(reflection_points)
        for key, value in reflection_points.items():
            if value == len(lines) - 1:
                sum += key * (1 if index % 2 == 0 else 100)

    logging.debug(sum)

    return sum

if part == 1:
    part1()
elif part == 2:
    part2()