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

type_of_hands = [(lambda l: l.count(l[0]) == 5, "Five of a kind"), (lambda l: l.count(l[0]) == 4 or l.count(l[1]) == 4, "Four of a kind"),( lambda l: len(list(set(l))) == 2, "Full house"), (lambda l: l.count(l[0]) == 3 or l.count(l[1]) == 3 or l.count(l[2]) == 3, "Three of a kind"), (lambda l: len(list(set(l))) == 3, "Two pair"), (lambda l: len(list(set(l))) == 4, "One pair"), (lambda l: len(list(set(l))) == 5, "High card")]

type_of_hands_part_2 = [(lambda l: len(list(set(l) - {'J'})) <= 1, "Five of a kind"), (lambda l: len(list(set(l)-{'J'})) == 2 and (l.count(list(set(l)-{'J'})[0]) < 2 or l.count(list(set(l)-{'J'})[1]) < 2), "Four of a kind"), (lambda l: len(list(set(l)-{'J'})) == 2, "Full house"), (lambda l: len(list(set(l)-{'J'})) == 3 and (l.count(list(set(l)-{'J'})[0]) == 3 - l.count('J') or l.count(list(set(l)-{'J'})[1]) == 3 - l.count('J') or l.count(list(set(l)-{'J'})[2]) == 3 - l.count('J')), "Three of a kind"), (lambda l: len(list(set(l)-{'J'})) == 3, "Two pair"), (lambda l: len(list(set(l)-{'J'})) == 4, "One pair"), (lambda l: len(list(set(l))) == 5, "High card")]

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
        for index, (type_of_hand, name) in enumerate(type_of_hands):
            if type_of_hand(hand):
                rank = len(type_of_hands)-index
                logging.debug(f"{hand} is {name} with hand rank {rank} and score {get_points_of_hand(hand)}")
                all_inclusive.append((hand, bids[hand_index], rank, get_points_of_hand(hand)))
                break

    all_inclusive.sort(key = lambda p: (p[2], p[3]))
    logging.debug(all_inclusive)
    for index, value in enumerate(all_inclusive):
        logging.debug(f"rank: {index+1} for {value[0]} (which is a {type_of_hands[len(type_of_hands)-value[2]][1]}) with bid {value[1]}: {value[1]*(index+1)}")
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
        for index, (type_of_hand, name) in enumerate(type_of_hands_part_2):
            if type_of_hand(hand):
                rank = len(type_of_hands)-index
                #rank = len(type_of_hands)-index+hand.count('J')
                #print(rank)
                #name = type_of_hands[index-hand.count('J')][1]
                logging.debug(f"{hand} is {name} with hand rank {rank} and score {get_points_of_hand(hand, values_part2)}")
                all_inclusive.append((hand, bids[hand_index], rank, get_points_of_hand(hand, values_part2)))
                break

    all_inclusive.sort(key = lambda p: (p[2], p[3]))
    logging.debug(all_inclusive)
    for index, value in enumerate(all_inclusive):
        logging.debug(f"rank: {index+1} for {''.join(sorted(str(value[0]).replace('J', '')))} (which is a {type_of_hands[len(type_of_hands)-value[2]][1]}) with bid {value[1]}: {value[1]*(index+1)}")
    return sum([int(value[1])*(index+1) for index, value in enumerate(all_inclusive)])


if part == 1:
    part1()
elif part == 2:
    part2()