def letter_in_word(guess,word):
    
    '''Returns true if guess is one of the letters in the word.
    Otherwise, it returns false'''

    if guess in word:
        print(True)
    else:
        print(False)
                
def hint(color,secret):
    '''Returns whether or not the color is in the secret'''
    if color in secret:
        print("The color " + str(color) + " IS in the sequence of colors")
    else:
        print("The color " + str(color) + " IS NOT in the sequence of colors")
