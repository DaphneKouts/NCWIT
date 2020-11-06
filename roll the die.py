#Daphne Koutsoukos
import random

def die_count(roll_list):
    roll = random.randint(1,6)
    roll_list[roll - 1] = roll_list[roll - 1] + 1
    return roll_list

def die_print(roll_list):
    print('''You rolled '''
    + str(roll_list[0]) + ''' ones, ''' 
    + str(roll_list[1]) + ''' twos, ''' 
    + str(roll_list[2]) + ''' threes, '''
    + str(roll_list[3]) + ''' fours, ''' 
    + str(roll_list[4]) + ''' fives, and ''' 
    + str(roll_list[5]) + ''' sixes.''')
    
def roll():
    done = 0
    roll_list = [0,0,0,0,0,0]
    num = input("How many times do you want to roll the die? ")
    while done < num:
        roll_list = die_count(roll_list)
        done = done + 1
    print(die_print(roll_list))
    