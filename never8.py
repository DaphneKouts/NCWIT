######
# Strategy Game: Never8
#
# never8.py implements a round-robin tournament of Never 8
# To run a tournament, execute never8_play.py, not this file.
# The students and teacher should modify never8_play.py and not modify this file.
#
# Each player should have their own .py file containing 
# a function called move(my_history, their_history)
# These filenames (without the .py extension) are passed to the 
# round_robin() function as the 2nd, 3rd, etc. arguments.
# 
# Author:  K. Holmes
# Date:    11 December 2018
# Modelled on PLTW's RPS
#######


def round(round_number, player1, player2, history1=[0], history2=[0]):
    ''' Plays one round of Never8
    player1 and player2 are functions that each accept two integers and return an 
    int representing their score for the current round.  score1 and score2 are the 
    two players' histories against each other, the sum of which is their current score
    
    Returns move1, move2, score1, score2
        move1, move2 are single characters: the moves made by the two players
        score1 and score2 are each -1, 0, or +1 for loss, tie, win
    '''
    # Get each player's current score
    p1_score = calculate_current_score(history1)
    p2_score = calculate_current_score(history2)
    
    # Get player 1's move. 
    move1 = player1(round_number, p1_score, p2_score)
    if len(history1) == 1 and history1[0] == -1:
        history1 = [move1]
    else:
        history1 = history1 + [move1]
    p1_score += move1
    
    # Get player 2's move. 
    move2 = player2(round_number, p1_score, p2_score)     ################################################################################
    if len(history2) == 1 and history2[0] == -1:
        history2 = [move2]
    else:
        history2 = history2 + [move2]
    p2_score += move2
    
    # return the history and current score for each player           
    return p1_score, p2_score, history1, history2

def calculate_current_score(history):
    ''' return the sum of the list.  history is a list of values the player
    has earned in all previous rounds.
    '''
    total = 0
    if len(history) == 1 and history[0] == -1:
        return 0
    for score in history:
        total += score
    return total
    
def new_record(record1, record2, move1, move2):
    ''' 
    Calculate the current win/loss/tie tuple for each player 
    record1 and record2 are the current win,loss,tie totals tuple
    move1 and move2 are the amount each scored in this round
    return the updated record1 and record2
    '''
    if move1 > move2:                            # Player1 won the round
        record1=(record1[0]+1,record1[1], record1[2])#win,loss,tie
        record2=(record2[0],record2[1]+1, record2[2])
    elif move2 > move1:                          # Player2 won the round
        record1=(record1[0],record1[1]+1, record1[2])
        record2=(record2[0]+1,record2[1], record2[2])
    else:                                        # tie
        record1=(record1[0],record1[1], record1[2]+1)
        record2=(record2[0],record2[1], record2[2]+1)
    return record1, record2

def playoff(player1, player2, number_of_rounds=60):
    '''
    player1 and player2 are functions that accept two ints and return an int
    number_of_rounds is an int
    Plays a sequence of rounds between two players
    
    Returns record1, record2, my_history1, my_history2
         where record1, record2 are win-loss-tie tuples
         my_history1, my_history2 are strings representing what the players did
    '''
    record1, record2 = (0,0,0),(0,0,0) #win,loss,tie
    history1, history2 = [0], [0]
    for round_number in range(number_of_rounds):
        move1, move2, history1, history2 = round(round_number, player1, player2, history1, history2 )
        record1, record2 = new_record(record1, record2, move1, move2)        
    return record1, record2, history1, history2
    
def team_name(module):
    '''
    Accepts a module that has been imported
    Returns the name of the module as a string
    '''
    return str(module).split(' ')[1].replace('\'','')

def strategy_name(module):
    '''
    Accepts a module that has been imported
    Returns the value of strategy_name in the imported file <module>
    '''
    return module.strategy_name
    
def make_history_string(history):
    ''' return a string version of the history list'''
    strHistory = ''
    for score in history:
        strHistory += str(score) + ', '
    return strHistory[0:len(strHistory)-2]   # remove the last comma

def count_zeros(history):
    ''' FOR JAKE: return the number of zerors in history list'''
    numZeros = 0
    for score in history:
        if score == 0:
            numZeros += 1
    return numZeros
    
        
def round_robin(number_of_rounds, *argv):
    '''number_of_rounds is an int = 1 or more
    The remaining arguments become a list: argv
    argv is a list of functions, one per player
    '''
    # Create report and scores[player1][player2] array
    scores = {} #scores[team_name] = [(W,L,T), (W,L,T), etc.]
    report = {} #report[team_name] = 'Report string'
    team_names = [] # list of the module names
    strategy_names = {}
    num_zeros = {} #number of zero rounds

    for player1 in argv:
        # Append the module name to the team_names list
        team_name1 = team_name(player1)     
        team_names.append(team_name1)
        
        #Place the strategy name in the dictionary, keyed by the module name
        strategy_names[team_name1]=player1.strategy_name
        
        #Provide the first line of the report
        report[team_name1] = 'Win-loss-tie report for '+team_name1+'   ' + player1.strategy_name +':\n'
        
        #Create an empty list that will get populated with (W,L,T) 3-tuples
        scores[team_name1] = []
        num_zeros[team_name1] = 0
    
    for player1 in argv:
        player1_name = team_name(player1) #repeat of above
        scores[player1_name].append('X')
        for player2 in argv[argv.index(player1)+1:]:
            player2_name = team_name(player2)
            
            record1, record2, history1, history2 = playoff(player1.move, player2.move, number_of_rounds)
            scores[player1_name].append(record1)
            scores[player2_name].append(record2)
            score1 = str(record1[0])+'-'+str(record1[1])+'-'+str(record1[2])
            score2 = str(record2[0])+'-'+str(record2[1])+'-'+str(record2[2])
            
            report[player1_name] += '\n'+ player1_name + ' '+ strategy_name(player1)+ ': '+ ' '*8  + ' '+score1+'\n' + make_history_string(history1)  + \
                                    '\n'+ player2_name + ' '+ strategy_name(player2) +': '+ ' '*8 + make_history_string(history2)+' \n'
                                    
            report[player2_name] += '\n'+ player2_name + ' '+ strategy_name(player2)+ ': '+ ' '*8  + ' '+score2+'\n' + make_history_string(history2)  + \
                                    '\n'+ player1_name + ' '+ strategy_name(player1) +': '+ ' '*8 + make_history_string(history1)+' \n'
            num_zeros[player1_name] += count_zeros(history1)
            num_zeros[player2_name] += count_zeros(history2)
            
    overall_record = {}
    for team in report:
        total_score = [0,0,0]
        for score in scores[team]:
            if score != 'X':
                total_score[0] += score[0]
                total_score[1] += score[1]
                total_score[2] += score[2]
            overall_record[team] = total_score
    short_report = '-'*80+'\nWin-loss-tie report for round robin:\n\n'

    ''' 
    Calculate the total score from the tournament using the NHL approach
      win = +2
      tie = +1
      loss = +0
    '''
    for team in overall_record:
        short_report += str(overall_record[team][0])+\
                        '-'+str(overall_record[team][1])+\
                        '-'+str(overall_record[team][2])+\
                        '\t '+'Total score: '+str(overall_record[team][0]*2 + overall_record[team][2])+\
                        '\t '+team+': '+strategy_names[team]+'\n'
    return short_report, report, num_zeros, strategy_names
