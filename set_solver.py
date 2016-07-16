import random
from itertools import combinations

class Attribute(object):
    pass

class Color(Attribute):
    types = ['R','G','P']
    def __init__(self):
        self.red    = 'R'
        self.green  = 'G'
        self.purple = 'P'

class Style(Attribute):
    def __init__(self):
        self.filled = 'F'
        self.hashed = 'H'
        self.open   = 'O'

class Shape(Attribute):
    def __init__(self):
        self.squiggle = 'S'
        self.diamond  = 'D'
        self.oval     = 'O'

class Card(object):
    # colors  = tuple(Color().__dict__.values())
    # styles  = tuple(Style().__dict__.values())
    # shapes  = tuple(Shape().__dict__.values())
    colors  = ('R', 'G', 'P')
    styles  = ('F', 'H', 'O')
    shapes  = ('S', 'D', 'O')
    numbers = (1, 2, 3)

    def __init__(self, color, style, shape, number):
        assert(color  in Card.colors)
        assert(style  in Card.styles)
        assert(shape  in Card.shapes)
        assert(number in Card.numbers)


        self.color = color
        self.style  = style
        self.shape  = shape
        self.number = number

    def __eq__(self, other):
        return self.color == other.color and self.style == other.style and \
               self.number == other.number and self.shape == other.shape

    def __repr__(self):
        return '{0}{1}{2}{3}'.format(
            self.shape,
            self.color,
            self.number,
            self.style,
        )
        # return '\n'.join([
        #     'Color: {0}'.format(self.color),
        #     'Style: {0}'.format(self.style),
        #     'Shape: {0}'.format(self.shape),
        #     'Number: {0}'.format(self.number),
        # ])


cards = []
for i in range(10):
    color = random.choice(Card.colors)
    style = random.choice(Card.styles)
    shape = random.choice(Card.shapes)
    number = random.choice(Card.numbers)
    cards.append(Card(color, style, shape, number))

print(cards)

print('\n')

attrs = cards[0].__dict__.keys()

for combo in combinations(cards, 3):
    if any(len(set(getattr(card, attr) for card in combo)) == 2 for attr in attrs):
        continue
    for card in combo:
        print(repr(card), end=" ")
    print()

# cards = [
#     'SP3F',
#     'DP3O',
#     'DR2F',
#     'SP3H',
#     'DG3O',
#     'SR1H',
#     'SG2O',
#     'SP1F',
#     'SP3O',
#     'OR3O',
#     'OR3H',
#     'OR2H',
# ]
