import sys, logging, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log_level', default="INFO")
parser.add_argument('-t', '--testing', required=False, default=None)
args = parser.parse_args()

debug, part, testing = args.log_level, os.environ.get('part', 1), args.testing

logging.basicConfig(level=debug)

sum = 0

### PART 1
if part == 1:
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            pass
### PART 2
elif part == 2:
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            pass

if debug != "DEBUG":
    print(sum) # 
elif testing:
    assert sum == int(testing)
    print(f"Result {sum} is correct")