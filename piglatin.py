#Daphne Koutsoukos
def piglatin(aWord):
    '''Using this function, you can write a word in parenthesis and it will convert it to piglatin'''
    one = 1
    end = len(aWord)
    zero = 0
    print(aWord[one:end] + aWord[zero] + "ay")
def english(aWord):
    '''Using this function, you can convert the piglatin back to english'''
    end = len(aWord) - 3
    zero = 0
    print(aWord[end] + aWord[zero:end])
