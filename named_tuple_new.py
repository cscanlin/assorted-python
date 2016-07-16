import sys
import os
sys.path.insert(0, os.path.join(os.path.expanduser('~'), 'python_scripts'))
from cs_collections import namedtuple

format = '{rank} of {suit}s'
# format_template = '{name} of %rs'
Card = namedtuple('Card', ['rank', 'suit'], format=format)
# Card = namedtuple('Card', ['rank', 'suit'])
cards = [Card('1', 'club'), Card('5', 'diamond')]
for card in cards:
    # print(card)
    print(card)
