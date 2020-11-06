def successful_party(numPeanuts, isWeekend):
    '''This function allows you to see if the elephant party is successful by inputing the number of peanuts and the day of the week. '''
    
    if isWeekend == False:
        if 400 <= numPeanuts <= 600:
            print(str(numPeanuts) + " is " + str(True) + ", your party is successful. ")
        else:
            print(str(numPeanuts) + " is " + str(False) + ", your party is unsuccessful, weekdays need between 400 and 600 peanuts. ")
            
    else:
        if 700 <= numPeanuts:
            print(str(numPeanuts) + " is " + str(True) + ", your party is successful. ")
        else:
            print(str(numPeanuts) + " is " + str(False) + ", your party is unsuccessful, you need at least 700 peanuts on the weekend. ")