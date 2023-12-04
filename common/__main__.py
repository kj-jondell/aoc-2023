### TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
### TODO                                                   TODO
### TODO      1. Make into a module!                       TODO
### TODO      2.                                           TODO
### TODO      3.                                           TODO
### TODO      4.                                           TODO
### TODO      5.                                           TODO
### TODO                                                   TODO
### TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO

import requests, os, sys
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--day", type=int, required=True)
parser.add_argument("-p", "--part", type=int, default=1, required=False)
parser.add_argument("--get-instructions", required=False, action='store_true')
parser.add_argument("--get-input-data", required=False, action='store_true')
parser.add_argument("--send-response", required=False, action='store_true')

args = parser.parse_args()

day, part = args.day, args.part
try:
    session = f"session={os.environ['AOC_SESSION']}"
except KeyError:
    print("Please set a valid AOC_SESSION environment variable.\nExiting")
    sys.exit(0)

get_instructions, get_input_data, send_response = args.get_instructions, args.get_input_data, args.send_response

if get_instructions:
    response = requests.get(f"https://adventofcode.com/2023/day/{day}{'#part2' if part == 2 else ''}", headers={"Cookie" : session})
    soup = BeautifulSoup(response.content.decode("UTF-8"), features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    text = soup.get_text()
    print("\n".join(text.splitlines()[16:-10]))

if get_input_data:
    response = requests.get(f"https://adventofcode.com/2023/day/{day}/input", headers={"Cookie" : session})
    print(response.content.decode("UTF-8"))

if send_response:
    sum = sys.stdin.readline()
    response = requests.post(f"https://adventofcode.com/2023/day/{day}/answer", headers={"Cookie" : session}, data={"level": part, "answer": sum})
    print(response.content.decode("UTF-8"))
