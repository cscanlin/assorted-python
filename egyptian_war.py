import itertools
import random
import time

FACECARD_TRIES_DICT = {
    'Jack': 1,
    'Queen': 2,
    'King': 3,
    'Ace': 4,
}

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def is_face(self):
        return self.rank in FACECARD_TRIES_DICT.keys()

    def __str__(self):
        return '{0} of {1}s'.format(self.rank, self.suit.capitalize())

class Deck(object):
    suits = ['club', 'spade', 'heart', 'diamond']
    ranks = (list(range(2, 11)) + list(FACECARD_TRIES_DICT.keys()))

    def __init__(self, shuffle=False):
        self.cards = self.build_deck(shuffle=shuffle)

    def build_deck(self, shuffle):
        cards = [Card(*card_info) for card_info in itertools.product(self.ranks, self.suits)]
        if shuffle:
            random.shuffle(cards)
        return cards

    def deal(self, players):
        deal_cycle = itertools.cycle(players)
        for card in self:
            player_to_receive = next(deal_cycle)
            player_to_receive.add_card(card)

    def __iter__(self):
        for card in self.cards:
            yield card

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def list_cards(self):
        cards_str = '\n'.join('\t'+str(card) for card in self.cards)
        return 'player {name} has cards:\n{cards}'.format(name=self.name, cards=cards_str)

    def play_card(self):
        # time.sleep(.5)
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def __eq__(self, other):
        if self.name == other:
            return True

    def __str__(self):
        return self.name

    def __bool__(self):
        return True if self.cards else False

class HumanPlayer(Player):
    """docstring for HumanPlayer"""
    def __init__(self, name=None):
        if not name:
            name = input('what is your name?: ')
        super().__init__(str(name))

    def play_card(self):
        input('press enter to play a card')
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

class Hand(object):
    def __init__(self, game):
        self.num_to_play = 1
        self.pot = []
        self.pot_owner = None
        self.game = game

    def play(self):
        for player in self.cycle_active_players():
            last_card_played = self.turn(player)
            if self.pot_owner is not None and not last_card_played.is_face:
                return self.end_hand()
            if len(self.game.active_players) <= 1:
                self.pot_owner = player
                return self.end_hand()

    def cycle_active_players(self):
        start_index = self.game.active_players.index(self.game.starting_player)
        players_with_correct_start = self.game.active_players[start_index:] + self.game.active_players[:start_index]
        for player in itertools.cycle(players_with_correct_start):
            if player:
                yield player
            else:
                continue

    def turn(self, player):
        for i in range(self.num_to_play):
            if not player:
                break
            played_card = player.play_card()
            self.pot.append(played_card)
            print("{0} plays: {1}".format(player, played_card))
            print('num cards: {0}'.format(len(player.cards)))
            if played_card.is_face:
                self.pot_owner = player
                self.num_to_play = FACECARD_TRIES_DICT[played_card.rank]
                break
        return played_card

    def end_hand(self):
        for card in self.pot:
            self.pot_owner.add_card(card)
        return self.pot_owner, self.pot

class Game(object):
    def __init__(self):
        self.deck = Deck(shuffle=True)
        self.players = [Player(name) for name in ['p0', 'p1', 'p2', 'p3']]  # + [HumanPlayer('Chris')]
        self.deck.deal(self.players)
        self.starting_player = random.choice(self.players)

    @property
    def active_players(self):
        return [player for player in self.players if player]

    def play(self):
        while len(self.active_players) > 1:
            winner, pot = Hand(self.starting_player, self.active_players).play()
            print('{0} wins {1} cards\n'.format(winner, len(pot)))
            self.starting_player = winner
        print('final winner: {0}!'.format(winner))


if __name__ == '__main__':
    Game().play()
