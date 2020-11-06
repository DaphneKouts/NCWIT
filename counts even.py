#Daphne Koutsoukos

def count_evens(numbers):
    '''Give me a list of numbers in brackets'''
    even = 0
    odd = 0
    index = 0
    while index < len(numbers):
        if index%2 == 0:
            even = even + 1
        else:
            odd = odd + 1
        index = index + 1
    print("There are " + str(len(numbers)) + " in this list. There are " + str(even) + " even numbers and " + str(odd) + " odd numbers")
    
        