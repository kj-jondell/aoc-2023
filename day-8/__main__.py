import sys, os, logging

debug = os.environ.get('log_level', "DEBUG")
part = int(os.environ.get('part', "1"))

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