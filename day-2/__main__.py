import sys, re

amt_color = [("red", 12), ("green", 13), ("blue", 14)]
sum = 0

debug, part = False, 2

def get_game_id(line: str) -> int:
    return int(re.search(r'Game (\d+)*', line).group(1))

def get_amt_of_colors(line: str, color: str) -> list:
    return re.findall(r'(\d+) {}'.format(color), line)

### PART 1
if part == 1:
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            game_id = get_game_id(line)

            add_to_sum = True

            for color, amt in amt_color:
                for line_amt in get_amt_of_colors(line, color):
                    if int(line_amt) > amt:
                        if debug:
                            print(f"Game id: {game_id}, line amount {line_amt} {color} exceeds amount {amt}")
                        add_to_sum = False
                        break
                if not add_to_sum:
                    break

            if add_to_sum:
                sum += game_id

### PART 2
elif part == 2:
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            game_id = get_game_id(line)

            cube_sum = 1

            for color, amt in amt_color:
                line_amounts = [int(line_amt) for line_amt in get_amt_of_colors(line, color)]
                max_in_line = max(line_amounts)
                cube_sum *= max_in_line

            if debug:
                print(f"Game id: {game_id} cube sum: {cube_sum}")

            sum += cube_sum

if not debug:
    print(sum)