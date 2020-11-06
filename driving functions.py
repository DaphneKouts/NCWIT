#Daphne Koutsoukos

def drive(numMiles, gasInTank, MPG):
    gasInTank = numMiles - gasInTank
    return gasInTank

def addGas(gasInTank, tankSize):
    gasInTank = gasInTank/tankSize
    fill = tankSize - gasInTank
    if gasInTank <= .1:
        gasInTank = fill + gasInTank
    return gasInTank
        
def outOfGas(gasInTank):
    if gasInTank <= 0:
        gasInTank = 0
        return True, gasInTank
    else:
        return False, gasInTank
def main():
    loop = 0
    gasInTank = input("How much gas is in the tank?")
    MPG = input("how many MPG is your car?")
    tankSize = input("How big is your tank?")
    while loop < 4:
        numMiles = input("How many miles do you have to drive to reach the destiation?")
        gasInTank = drive(numMiles, gasInTank, MPG)
        empty, gasInTank = outOfGas(gasInTank)
        if outOfGas == True:
            addGas(gasInTank, tankSize)
            print("out of gas" + str(gasInTank))
        else:
            print(gasInTank)
        loop = loop + 1
