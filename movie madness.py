#Daphne Koutsoukos
def movie_tickets (you, friend): 
    '''this function allows you to know in advance if you will get great,ok or lose seats when going to a movie theater with your friend''' 
    if you <= 5 or friend <= 5:
        print("You are late, no seat are left. Try again another day.") 
        
    else: 
            if 5 < you < 35 and 5 < friend <35: 
                print("You got ok seats, enjoy the film") 
            else:
                print("You got the best seats in the house, enjoy") 