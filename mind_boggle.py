import random
import itertools
from collections import namedtuple

class BoggleTrick(object):

    def __init__(self):
        # self.deck = Deck(shuffle=True)
        self.deck = self.create_deck(shuffle=True)

        self.blacks = []
        self.black_random = []
        self.reds = []
        self.red_random = []

    def create_deck(self, shuffle=False):
        Card = namedtuple('Card', ['rank', 'suit'])

        ranks = (list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace'])
        suits = ['club', 'spade', 'heart', 'diamond']
        cards = [Card(*card_info) for card_info in itertools.product(ranks, suits)]
        if shuffle:
            random.shuffle(cards)
        return cards

    def parse_piles(self):
        it_deck = iter(self.deck)
        for card1, card2 in zip(it_deck, it_deck):
            if card1.suit in ['club', 'spade']:
                self.blacks.append(card1)
                self.black_random.append(card2)
            if card1.suit in ['heart', 'diamond']:
                self.reds.append(card1)
                self.red_random.append(card2)

    @property
    def smallest_random_pile(self):
        return min(len(self.red_random), len(self.black_random))

    def swap_cards(self):
        num_to_swap = random.randrange(self.smallest_random_pile)
        black_swap = [self.black_random.pop(random.randrange(len(self.black_random))) for _ in range(num_to_swap)]
        red_swap = [self.red_random.pop(random.randrange(len(self.red_random))) for _ in range(num_to_swap)]
        self.black_random += red_swap
        self.red_random += black_swap

    # @staticmethod
    # def print_cards(card_list):
    #     print(['{0} of {1}s'.format(card.rank, card.suit.capitalize()) for card in card_list])

# class Deck(object):
#     suits = ['club', 'spade', 'heart', 'diamond']
#     ranks = (list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace'])
#
#     def __init__(self, shuffle=False):
#         self.cards = self.build_deck(shuffle=shuffle)
#
#     def build_deck(self, shuffle):
#         cards = [Card(*card_info) for card_info in itertools.product(self.ranks, self.suits)]
#         if shuffle:
#             random.shuffle(cards)
#         return cards
#
#     def __iter__(self):
#         for card in self.cards:
#             yield card
#
#     def __str__(self):
#         return ', '.join([str(card) for card in self.cards])
#
# class Card(object):
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#
#     def __str__(self):
#         return '{0} of {1}s'.format(self.rank, self.suit.capitalize())

# class newnamedtuple(namedtuple):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

format_template = '{rank} of {suit}s'
Card = namedtuple('Card', ['rank', 'suit'], format_template=format_template)
cards = [Card('1', 'club'), Card('5', 'diamond')]
print(cards)
# print([fmt_str.format(rank=card.rank, suit=card.suit.capitalize()) for card in cards])

# boggle = BoggleTrick()
# boggle.parse_piles()
# boggle.swap_cards()
#
# print(boggle.red_random)
# print(boggle.black_random)
