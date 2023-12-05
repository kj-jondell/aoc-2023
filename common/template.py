from common import boilerplate
import os, logging, re, sys

part = os.environ.get('part', 1)

@boilerplate.part
def part1():
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            pass

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