'''The function move(my_history, their_history) must return 'r', 'p', or 's'.
my_history and their_history are strings of the same length, perhaps length zero.
'''
from random import randint

strategy_name = 'CGVB and CGVF'

def roll():
    return randint(1,6) + randint(1,6)

def move(round_number, my_score, their_score):
    '''This player only rolls if the score is less than 50.
    '''
    thisRound = 0
    done = False
    while thisRound < 39 and not done:
        throw = roll()
        if throw == 8:
            thisRound = 0
            done = True
        else:
            thisRound += throw
    return thisRound
    