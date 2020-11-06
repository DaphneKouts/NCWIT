#Daphne Koutsoukos

def find_diff(numbers):
    '''This function takes a list and prints the highest and lowest numbers with their difference'''
    Min = numbers[0]
    Max = numbers[0]
    diff = 0
    for num in numbers:
        if num > Max:
            Max = num
        if num < Min:
            Min = num
        diff = Max - Min
    print("The minimum is " + str(Min) + ", and the maximum is " + str(Max) + ". The difference between them is " + str(diff))