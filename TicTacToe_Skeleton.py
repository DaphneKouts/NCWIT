'''
Created on March 15, 2017
@author: KJHolmes
'''
##  This function takes in the list and prints the tictactoe board
#    board: the list that represents the tictactoe board
def print_TTT(board):
    print('''__''' + board[0][0] + '''___l___''' + board[0][1] + '''___l___''' + board[0][2] + '''__
              __''' + board[1][0] + '''___l___''' + board[1][1] + '''___l___''' + board[1][2] + '''__
              __''' + board[2][0] + '''___l___''' + board[2][1] + '''___l___''' + board[2][2] + '''__''')



## Adds a mark on the board if the spot is not already filled.  The board
## should not be changed if there is already a mark.
## return True if you can add a mark, False if the spot already had a mark.
#    r:  the row number (0 -> 2)
#    c:  the column number (0 -> 2)
#    mark:  "X" or "O"
#    board:  the list that represents the tictactoe board
def add_mark(r, c, mark, board):
    if board[r][c] != " ":
        return False, board
    else:
        board[r][c] = mark
        return True, board




##  Returns False if there is an open square, True there are no blank spots on the board
##  An open square is represented by a blank:  " "
#    board: the list that represents the tictactoe board
def isFull(board):
    full = True
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                full = False
    return full





###  YOU DO NOT NEED TO CHANGE THIS FUNCTION, but you may want to look at
#    it to see some sample code.
##  Returns true if there are three in a row on a row, a column or a diagonal
#   This version of the function works by comparing all the items in a 
#   row, column or diagonal to see if they are the same (but not blank)
#    board: the list that represents the tictactoe board
def game_over(board):
    for row in range(3):
        # if the first spot is not blank and all the values in the row are the same 
        #   then return true
        if ((board[row][0] != " ") and 
            (board[row][0]==board[row][1]) and 
            (board[row][0]==board[row][2])):
            return True
    for col in range(3):
        # if the first spot is not blank and all the values in the column are the same 
        #   then return true
       if ((board[0][col] != " ") and 
           (board[0][col]==board[1][col]) and 
           (board[0][col]==board[2][col])):
            return True
    # if the first spot is not blank and all the values in the diagonal are the same 
    #     then return true
    if ((board[0][0] != " ") and 
        (board[0][0]==board[1][1]) and 
        (board[0][0]==board[2][2])):
        return True
    #  Same, but going upper right to lower left
    if ((board[0][2] != " ") and 
        (board[0][2]==board[1][1]) and 
        (board[0][2]==board[2][0])):
        return True
    # Nothing won so return False
    return False




###  YOU DO NOT NEED TO CHANGE THIS FUNCTION, but you may want to look at
#    it to see some sample code.
###  The main program  
#    board: the list that represents the tictactoe board
#    mark:  X or O.  X always starts
def ttt():
    #
    #  initialize all the variables
    #
    board = [[" ", " ", " "],[ " ", " ", " "],[ " ", " "," "]]
    print_TTT(board)
    mark = "X"
    print("Welcome to Tic Tac Toe")

    # "Q" will force it to exit
    # This loop keeps going until the game is over

    while mark != "Q":
        #  good_val will be set to True when a valid place on the board is given
        good_val = False
        while not good_val:
            print(" ")
            # subtract 1 because the index starts counting at 0 and people start counting at 1
            r = int(input("row:  "))-1
            c = int(input("column: "))-1
            print(" ")

            #  Check if the row & column are invalid
            if not((0 <= r <=2 ) and (0 <= c <=2 )):            # Remember, we subtracted 1 from r and c
                print("The row and column must be 1, 2, or 3")  

            #  Check if the place was already filled
            else:
                ok, board = add_mark(r, c, mark, board)
                if not(ok):
                    print("There was already a mark there.  Pick a new place.")
                else:
                    # place is accepted - note that the add_mark function added it to 
                    #       the board if it could, so the mark has already been added.
                    #       add_mark was called as part of the elif above.
                    good_val = True 
        ##  end of inner while loop
        
        print_TTT(board)
        print(" ")
        
        # call isFull to see if the board is full (might be a tie) and 
        # game_over is called to figure out if someone won.  If either is true, 
        # set mark to "Q" to force the outer loop to exit.
        full = isFull(board)
        win = game_over(board)
        if (win):
            print(mark + " Wins!")
            mark = "Q"
        elif (full):
            print("It's a tie!")
            mark = "Q"
        #  No one won and there are still spaces open, so switch the mark
        elif (mark == "O"):
            mark = "X"
        else: 
            mark = "O"
    ## end of outer while loop

    print("game over!")

ttt()