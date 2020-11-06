######
# Strategy Game: Never8
#
# Execute this file never8_play.py to play a tournament.
# never8.py implements the round robin tournament of never8
# 
# Prior to execution:
# Line 22: Type each team's module name (the file name, but without the py) on the import statement,
# Lines 27-30: Create a reload() statement for each module, and
# Original line 36: Place each module name as an arugment to the function never8.round_robin().
# Each player should have their own .py file containing 
# a function called move(my_score, their_score)
# These filenames (without the .py extension) are passed to the 
# round_robin() function as the 2nd, 3rd, etc. arguments.
#
# Author:  K. Holmes
# Date:    11 December 2018
# Modelled on PLTW's RPS
#######

import never8
reload(never8)

import Team01, Team02, Team03, Team04, Team05  # These are file names in this folder     
#import Team06, Team07, Team08, Team09, Team10  # These are file names in this folder     
#import Team11, Team12, Team13                   # These are file names in this folder     
# The reload() statement is needed for each team because import 
# will only compile source code once to create the pyc file and store in memory.
# Without reload(), changes to the .py file will be ignored unless the pyc 
# file is deleted and the kernel restarted. 
reload(Team01) 
reload(Team02)
reload(Team03)
reload(Team04)
reload(Team05)
'''
reload(Team06) 
reload(Team07)
reload(Team08)
reload(Team09)
reload(Team10)
reload(Team11) 
reload(Team12)
reload(Team13)
'''


team_summary = {}
zeros_summary = {}
team_win_summary = {}
#for team in [Team01,  Team02, Team03, Team04, Team05,Team06, Team07, Team08, Team09, Team10,Team11, Team12, Team13]:
for team in [Team01,  Team02, Team03, Team04, Team05]:
    # Append the module name to the team_names list
    team_name = never8.team_name(team)     
    team_summary[team_name]=0
    team_win_summary[team_name]=0
    zeros_summary[team_name]=0
NUMBER_OF_CONTESTS = 100
for i in range(NUMBER_OF_CONTESTS):                      
    # The first argument of round_robin() specifies the number of 
    # rounds to be played by each pair of strategies. 
    # Change the other arguments to use more teams, fewer teams, or different teams
    #short_report, long_report, zeros, strategy_names = never8.round_robin(NUMBER_OF_CONTESTS, Team01,  Team02, Team03, Team04, Team05,Team06, Team07, Team08, Team09, Team10,Team11, Team12, Team13)        
    short_report, long_report, zeros, strategy_names = never8.round_robin(NUMBER_OF_CONTESTS, Team01,  Team02, Team03, Team04, Team05)        
    '''
    #print long_report
    for team in long_report:
        print '-'*80
        print long_report[team]
    '''   
    #Calculate the team win summaries
    pos = 0
    winScore = 0
    for team in long_report:
        pos = short_report.find("Total score: ",pos) + 12
        team_summary[team] += int(short_report[pos:pos+4])
        if winScore < int(short_report[pos:pos+4]):
            winScore = int(short_report[pos:pos+4])
            winTeam = team
    team_win_summary[winTeam] += 1

    ###  commented out the zeros report
    '''out = "Round: "+ str(i)+ ':   '
    for team in long_report:
        out += team+"\t"+str(zeros[team]) +';\t'
        zeros_summary[team] += zeros[team]
    print(out[:len(out)-2])'''

###  print the multi-round summary

print('\n'+30*'='+'\nTotal points out of '+str(NUMBER_OF_CONTESTS)+' contests:')
for team in long_report:
    print(team+"\t "+str(team_summary[team])+"\t Wins:  " +str(team_win_summary[team])+"\t"+strategy_names[team])

# calculate & print the team with the highest score
most_points = 0
winning_team = ""
for team in long_report:
    if team_summary[team] > most_points:
        most_points = team_summary[team]
        winning_team = team
print("*"*50)
print("\n THE WINNING TEAM IS "+winning_team+" with "+str(most_points)+" points.  Congratulations, "+strategy_names[winning_team]+"!")

