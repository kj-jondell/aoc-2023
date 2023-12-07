import sys, logging, os
import argparse, functools

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log_level', default="INFO")
parser.add_argument('-t', '--testing', required=False, default=None)
args = parser.parse_args()

debug, testing = args.log_level, args.testing

logging.basicConfig(level=debug)

def part(child_fn):
    @functools.wraps(child_fn)
    def wrapper():
        sum = child_fn()

        logging.debug(sum)

        if debug != "DEBUG":
            print(sum) # 
        elif testing:
            assert sum == int(testing)
            print(f"Result {sum} is correct")

        return sum
    return wrapper