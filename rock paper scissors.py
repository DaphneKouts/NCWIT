#Daphne Koutsoukos

def RPS():
    import random
    choices = ["rock","paper","scissors"]
    computerChoice = random.choice(choices)
    player = raw_input("Pick rock, paper, or scissors: ")
    if player == computerChoice:
        return "Tie"
    elif computerChoice == "rock" and player == "paper":
        return "You win, computer chose rock"
    elif computerChoice == "rock" and player == "scissors":
        return "Computer wins, computer chose rock"
    elif computerChoice == "scissors" and player == "rock":
        return "You win, computer chose scissors"
    elif computerChoice == "scissors" and player == "paper":
        return "Computer wins, computer chose scissors"
    elif computerChoice == "paper" and player == "rock":
        return "Computer wins, computer chose paper"
    else:
        return "You win, computer chose paper"
    