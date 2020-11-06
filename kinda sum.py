def KindaSum():
    '''This function adds two integers together to get a "kinda" sum'''
    a = input("What is your first integer? ")
    b = input("What is your second integer? ")
    RealSum = a + b
    twenty = 20
    bonus = 23 * 2
    if RealSum < 10:
        print(RealSum)
    if RealSum > 19 and RealSum == 23:
        print(bonus)
    if 10 <= RealSum <= 19:
        print(twenty)
    if RealSum > 19 and RealSum != 23:
        print(RealSum)
    