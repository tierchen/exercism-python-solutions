import re
from collections import Counter
card_table = [[rank + suit for rank in '2_3_4_5_6_7_8_9_10_J_Q_K_A'.split('_')] for suit in 'SHCD']

translate = {'J': '11', 'Q': '12', 'K': '13', 'A': '14'}


def _of_a_kind(cards, m):
    kinds = [rank for rank, cnt in Counter(rank for rank, _ in cards).items() if cnt >= m]
    if not kinds:
        return 0
    return max(kinds)


def _twice_of_a_kind(cards, m, n):
    m, n = sorted([m, n], reverse=True)
    first_kind = _of_a_kind(cards, m)
    if not first_kind:
        return 0, 0
    working = [(rank, suit) for rank, suit in cards if rank != first_kind]
    second_kinds = _of_a_kind(working, n)
    if not second_kinds:
        return 0, 0
    return first_kind, second_kinds


def is_straight_flush(cards):
    straight = is_straight(cards)
    if is_straight(cards) and set(is_flush(cards)).pop() != 0:
        return straight
    return 0


def is_four_of_a_kind(cards):
    return _of_a_kind(cards, 4)


def is_full_house(cards):
    return _twice_of_a_kind(cards, 3, 2)


def is_flush(cards):
    if len(set(suit for _, suit in cards)) == 1:
        return tuple(sorted([rank for rank, _ in cards], reverse=True))
    return 0, 0, 0, 0, 0


def is_straight(cards):
    ranks_in_a_row = tuple(sorted([rank for rank, _ in cards], reverse=True))
    if ranks_in_a_row == tuple(reversed(range(ranks_in_a_row[-1], ranks_in_a_row[0] + 1))):
        return ranks_in_a_row[0]
    elif ranks_in_a_row == (13, 5, 4, 3, 2):
        return 5
    return 0


def is_three_of_a_kind(cards):
    return _of_a_kind(cards, 3)


def is_two_pair(cards):
    return _twice_of_a_kind(cards, 2, 2)


def is_one_pair(cards):
    return _of_a_kind(cards, 2)


def high_card(cards):
    return max(rank for rank, _ in cards)


combinations = [is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pair, is_one_pair, high_card]


def poker(hands_pre):
    hands = [[(int(translate.get(rank, rank)), suit)
              for card in hand
              for rank, suit in [re.match(r'(\d+|J|Q|K|A)(\w)', card).groups()]]
             for hand in hands_pre]
    print(hands)
    combs = [[f(cards) for f in combinations] for cards in hands]
    print(combs)
    winner_comb = max(combs)
    return [hands_pre[i] for i in (i for i, comb in enumerate(combs) if comb == winner_comb)]


print(poker(['JD QH JS 8D QC'.split(), 'JS QS JC 2D QD'.split()]))