#Daphne Koutsoukos
import random
def RockPaperScissors(name):
        '''insert your name inn quotes to play a game of rock paper scissors'''
        #initialize variables
        rounds = 0
        MAX_ROUNDS = 5
        #Do a loop for rounds
        while rounds < MAX_ROUNDS:
            myScore = 0
            vsScore = 0
            options = ["rock","paper","scissors"]
            #get input from user hit or run
            me = raw_input("rock, paper, or scissors: ")
            vs = random.choice(options)
            if me == "rock" and vs == "scissors":
                myScore += 1
                print("Computer chose: " + vs)
            elif me =="rock" and vs == "paper":
                vsScore += 1
                print("Computer chose: " + vs)
            elif me == "rock" and vs == "rock":
                draw = random.randint(1,3)
                if draw == 1:
                    myScore += 1 
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
                else:
                    vsScore += 1
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
            elif me == "paper" and vs == "rock":
                myScore += 1
                print("Computer chose:" + vs)
            elif me == "paper" and vs == "scissors":
                vsScore += 1
                print("Computer chose: " + vs)
            elif me == "paper" and vs == "paper":
                draw = random.randint(1,3)
                if draw == 1:
                    myScore += 1
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
                else:
                    vsScore += 1
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
            elif me == "scissors" and vs == "rock":
                vsScore += 1
                print("Computer chose: " + vs)
            elif me == "scissors" and vs == "paper":
                myScore += 1
                print("Computer chose: " + vs)
            elif me == "scissors" and vs == "scissors":
                draw = random.randint(1,3)
                if draw == 1:
                    myScore += 1
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
                else:
                    vsScore += 1
                    print("It is a draw, so the point was given randomly. Computer chose: " + vs)
            rounds += 1
            #Determine winner and print it
        if myScore > vsScore:
            print(str(name) + " is the winner")
        else:
            print("Computer is the winner")
