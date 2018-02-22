import re
from collections import Counter


class Hand:
    _translate = {'J': '11', 'Q': '12', 'K': '13', 'A': '14'}

    def __init__(self, hand):
        self.hand = [(int(self._translate.get(rank, rank)), suit)
                     for card in hand
                     for rank, suit in [re.match(r'(\d+|J|Q|K|A)(\w)', card).groups()]]

    @property
    def ranks(self):
        return tuple(sorted((rank for rank, _ in self.hand), reverse=True))

    def remain(self, exclude_rank):
        return Hand([str(rank) + suit for rank, suit in self.hand if rank != exclude_rank])

    def _of_a_kind(self, m):
        kinds = [rank for rank, cnt in Counter(rank for rank, _ in self.hand).items() if cnt >= m]
        if not kinds:
            return
        return (max(kinds), *self.remain(max(kinds)).ranks)

    def _twice_of_a_kind(self, m1, m2):
        m1, m2 = sorted([m1, m2], reverse=True)
        first_kind = self._of_a_kind(m1)
        if not first_kind:
            return
        rest = self.remain(first_kind[0])
        second_kind = rest._of_a_kind(m2)
        if not second_kind:
            return
        return (first_kind[0], second_kind[0], *self.remain(second_kind[0]).ranks)

    def is_straight_flush(self):
        straight = self.is_straight()
        if straight and set(self.is_flush()).pop() != 0:
            return straight
        return 0

    def is_four_of_a_kind(self):
        kind = self._of_a_kind(4)
        return kind if kind else (0, 0)

    def is_full_house(self):
        kinds = self._twice_of_a_kind(3, 2)
        return kinds if kinds else (0, 0)

    def is_flush(self):
        if len(set(suit for _, suit in self.hand)) == 1:
            return tuple(sorted([rank for rank, _ in self.hand], reverse=True))
        return 0, 0, 0, 0, 0

    def is_straight(self):
        if self.ranks == tuple(reversed(range(self.ranks[-1], self.ranks[0] + 1))):
            return self.ranks[0]
        elif self.ranks == (13, 5, 4, 3, 2):
            return 5
        return 0

    def is_three_of_a_kind(self):
        kind = self._of_a_kind(3)
        return kind if kind else (0, 0, 0)

    def is_two_pair(self):
        kinds = self._twice_of_a_kind(2, 2)
        return kinds if kinds else (0, 0, 0)

    def is_one_pair(self):
        kind = self._of_a_kind(2)
        return kind if kind else (0, 0, 0, 0)

    def high_card(self):
        return self.ranks

    combinations = [is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind,
                    is_two_pair, is_one_pair, high_card]


def poker(hands_pre):
    hands = [Hand(hand) for hand in hands_pre]
    combs = [[f(hand) for f in hand.combinations] for hand in hands]
    winner_comb = max(combs)
    return [hands_pre[i] for i in (i for i, comb in enumerate(combs) if comb == winner_comb)]
