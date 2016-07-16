import random
from time import sleep

class Game(object):
    def __init__(self):
        self.home_team_score = 0
        self.away_team_score = 0
        self.minute = 0

    def increment(self):
        self.minute += 1
        print(str(self.minute) + "'")
        chance = random.randint(0, 20)
        if chance == 20:
            self.home_team_score += 1
            print "GOAL!" + self.score
        elif chance == 19:
            self.away_team_score += 1
            print "GOAL!" + self.score

    @property
    def score(self):
        return "{}-{}".format(self.home_team_score, self.away_team_score)

game = Game()

while game.minute < 45:
    game.increment()
    sleep(.2)
print "HT " + game.score

while game.minute < 90:
    game.increment()
    sleep(.2)
print "FT " + game.score

# def time(min, home_team_score, away_team_score, score):
#     min = min + 1
#     print str(min) + "'"
#     chance = random.randint(0, 20)
#     if chance == 20:
#         home_team_score = home_team_score + 1
#         print "GOAL!" + score
#     elif chance == 19:
#         away_team_score = away_team_score + 1
#         print "GOAL!" + score
#     return min, home_team_score, away_team_score, score
# min = 0
# home_team_score = 0
# away_team_score = 0
# score = "{}-{}".format(home_team_score, away_team_score)
# while min < 45:
#     time()
#     sleep(.)
# print "HT " + score
# while min < 90:
#     time()
#     sleep(1)
# print "FT " + score
