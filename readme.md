# ADVENT OF CODE 2023

My solutions to this year's [advent of code](https://adventofcode.com/2023/).

## Usage

Use environment variables `AOC_SESSION`, `day`, `part` and `log_level` when running the following commands:
- To get instructions for `day` and part `part`: `python3 common -d $day -p $part --get-instructions > day-$day/instructions.txt`
- To get input data for `day`: `python3 common -d $day --get-input-data > day-$day/input.txt`
- To send answer for `day`: `cat day-$day/input.txt | python3 day-$day | python3 common -d $day -p $part --send-response`

## TODO
- Get and display leaderboard through AoC API
