from common import boilerplate
import os, logging, re, sys

part = int(os.environ.get('part', 1))

values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
values_part2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def get_points_of_hand(hand: str, value_list: list = values):
    sum = []
    for value in hand:
        sum.append(value_list[::-1].index(value))
    return sum

types = [(1, [5], "Five of a kind"), (2, [1, 4], "Four of a kind"), (2, [2, 3], "Full house"), (3, [1, 1, 3], "Three of a kind"), (3, [1, 2, 2], "Two pairs"), (4, [1, 1, 1, 2], "One pair"), (5, [1, 1, 1, 1, 1], "High score")]

def get_type_of_hand(hand: str, with_joker: bool = False):
    if not with_joker:
        symbols = set(hand)
        logging.debug(hand)
        for index, (amt, setup, name) in enumerate(types):
            if len(list(symbols)) == amt and sorted([hand.count(p) for p in list(symbols)]) == setup:
                return index, name
    else:
        symbols = set(hand) - {'J'}
        if not symbols: #edge case JJJJJ
            return 0, types[0][2]
        for index, (amt, setup, name) in enumerate(types):
            if len(list(symbols)) == amt:
                count_of_symbols = sorted([hand.count(p) for p in list(symbols)])
                count_of_symbols[-1] += hand.count('J')
                logging.debug(f"{sorted(count_of_symbols)} and {setup}")
                if count_of_symbols == setup:
                    return index, name

#Five of a kind, where all five cards have the same label: AAAAA
#Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#High card, where all cards' labels are distinct: 23456

@boilerplate.part
def part1():
    hands, bids = [], []
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            for hand, bid in re.findall(r'([a-zA-Z0-9]+) (.+)', line):
                hands.append(hand)
                bids.append(int(bid))

    all_inclusive = []

    for hand_index, hand in enumerate(hands):
        index, type_of_hand = get_type_of_hand(hand)
        rank = len(types)-index

        logging.debug(f"{hand} is a {type_of_hand}")
        all_inclusive.append((hand, bids[hand_index], rank, get_points_of_hand(hand)))
    
    all_inclusive.sort(key = lambda p: (p[2], p[3]))
    logging.debug(all_inclusive)
    for index, value in enumerate(all_inclusive):
        logging.debug(f"rank: {index+1} for {value[0]} (which is a {types[len(types)-value[2]][2]}) with bid {value[1]}: {value[1]*(index+1)}")
    return sum([int(value[1])*(index+1) for index, value in enumerate(all_inclusive)])

@boilerplate.part
def part2():
    hands, bids = [], []
    for line in sys.stdin:
        line = line.strip()
        if len(line)>0:
            for hand, bid in re.findall(r'([a-zA-Z0-9]+) (.+)', line):
                hands.append(hand)
                bids.append(int(bid))

    all_inclusive = []

    for hand_index, hand in enumerate(hands):

        logging.debug(f"{hand}")
        index, type_of_hand = get_type_of_hand(hand, True)
        rank = len(types)-index

        logging.debug(f"{hand} is a {type_of_hand}")
        all_inclusive.append((hand, bids[hand_index], rank, get_points_of_hand(hand, values_part2)))
    
    all_inclusive.sort(key = lambda p: (p[2], p[3]))
    logging.debug(all_inclusive)
    for index, value in enumerate(all_inclusive):
        logging.debug(f"rank: {index+1} for {value[0]} (which is a {types[len(types)-value[2]][2]}) with bid {value[1]}: {value[1]*(index+1)}")
    return sum([int(value[1])*(index+1) for index, value in enumerate(all_inclusive)])

if part == 1:
    part1()
elif part == 2:
    part2()