import sys, re #, itertools

debug, part = False, 1

def is_symbol_adjacent(symbol: dict, part_number: dict) -> bool:
    return symbol["x"] in range(part_number["x"] - 1, part_number["x"] + length + 1) and symbol["y"] in range(part_number["y"] - 1, part_number["y"] + 2)

def get_part_numbers_and_symbols(symbols_regex: str) -> tuple:
    part_numbers, symbols = [], []
    for y, line in enumerate(sys.stdin):
        line = line.strip()
        if len(line)>0:
            numbers = re.finditer(r'\d+', line)
            matched_symbols = re.finditer(symbols_regex, line)

            for match in numbers:
                part_numbers.append({"x" : match.start(), "y" : y, "number" : int(match.group())})
            for match in matched_symbols:
                symbols.append({"x" : match.start(), "y" : y, "symbol" : match.group()})

    return part_numbers, symbols

### PART 1
if part == 1:
    part_numbers, symbols = get_part_numbers_and_symbols(r'[^0-9.]') # matches all non-digits and non-dots

    sum = 0
    for part_number in part_numbers:
        length = len(str(part_number["number"]))
        for symbol in symbols:
            if debug:
                print(symbol, part_number)
            if is_symbol_adjacent(symbol, part_number):
                sum += part_number["number"] 
                break

### PART 2
elif part == 2:
    part_numbers, symbols = get_part_numbers_and_symbols(r'[*]')

    sum = 0
    for symbol in symbols:
        adjacent_numbers = []
        for part_number in part_numbers:
            length = len(str(part_number["number"]))
            if is_symbol_adjacent(symbol, part_number):
                    adjacent_numbers.append(part_number["number"])
        if len(adjacent_numbers) == 2:
            sum += adjacent_numbers[0] * adjacent_numbers[1]
        if debug:
            print(adjacent_numbers, sum)

if not debug:
    print(sum)