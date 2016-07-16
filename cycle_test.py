import random
from collections import OrderedDict

# def play_hand(players, current_turn):
#     hand = {}
#     for _, i in enumerate(players):
#         print(current_turn)
#         hand[players[current_turn]] = random.randint(0, 5)  # this could alternatively be player.turn() or something
#         if current_turn < len(players)-1:
#             current_turn += 1
#         else:
#             current_turn = 0
#
#     winning_player = max(hand, key=hand.get)
#     print(hand)
#     return winning_player

def play_hand(players, starting_player):
    hand = OrderedDict()
    start_index = players.index(starting_player)
    for player in players[start_index:] + players[:start_index]:
        player_score = random.randint(0, 5)  # this could alternatively be player.turn() or something
        hand[player] = player_score
        print("{0} plays: {1}".format(player, player_score))
    winner = max(hand, key=hand.get)  # gets the player with the highest score
    print('hand results: {0}'.format(hand))
    print('winner: {0}\n'.format(winner))
    return winner

if __name__ == '__main__':
    players = ['p0', 'p1', 'p2', 'p3']
    starting_player = 'p0'
    for i in range(5):  # play 5 hands
        winner = play_hand(players, starting_player)
        starting_player = winner
