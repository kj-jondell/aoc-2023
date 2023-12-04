import sys, re

debug, part = False, 2

sum = 0

if part == 1:
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0:
            card_id, winning_numbers, my_numbers = re.findall(r'Card\s*(\d+): (.+) \| (.+)', line)[0]

            winning_numbers = set([int(number) for number in winning_numbers.split()])
            my_numbers = set([int(number) for number in my_numbers.split()])
            
            sum += int(2**(len(my_numbers.intersection(winning_numbers))-1))
elif part == 2:
    matches = []
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0:
            card_id, winning_numbers, my_numbers = re.findall(r'Card\s*(\d+): (.+) \| (.+)', line)[0]

            winning_numbers = set([int(number) for number in winning_numbers.split()])
            my_numbers = set([int(number) for number in my_numbers.split()])
            no_matches = len(my_numbers.intersection(winning_numbers))

            matches.append((1, no_matches)) # tuples consisting of (no_copies, no_matches)
            
    for index, num in enumerate(matches):
        matches = matches[:index+1]+[(copies+matches[index][0], inner_num) for copies, inner_num in matches[index+1:index+num[1]+1]]+matches[index+num[1]+1:]
        sum += matches[index][0]
print(sum)
