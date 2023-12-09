from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

@boilerplate.part
def part1():
    sum = 0
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            working_list = [int(value) for value in line.split()]
            difference_list = []
            while set(working_list) != {0}:
                difference_list.append(working_list[:])
                working_list = [working_list[index+1] - num for index, num in enumerate(working_list[:-1])]

            rev_diff = difference_list[::-1]
            for index, cmp_list in enumerate(rev_diff[:-1]):
                next_list = rev_diff[index+1]
                next_list += [next_list[-1] + cmp_list[-1]]

            sum += rev_diff[-1][-1]

    logging.debug(sum)
    return sum


@boilerplate.part
def part2():
    sum = 0
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            working_list = [int(value) for value in line.split()]
            difference_list = []
            while set(working_list) != {0}:
                difference_list.append(working_list[:])
                working_list = [working_list[index+1] - num for index, num in enumerate(working_list[:-1])]

            rev_diff = difference_list[::-1]
            for index, cmp_list in enumerate(rev_diff[:-1]):
                next_list = rev_diff[index+1]
                next_list.insert(0, next_list[0] - cmp_list[0])

            logging.debug(rev_diff)

            sum += rev_diff[-1][0]

    logging.debug(sum)
    return sum


if part == 1:
    part1()
elif part == 2:
    part2()