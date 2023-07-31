





def FindLCM(firstNumber, secondNumber):
    LCM = {}
    biggestNumber = firstNumber
    smallerNumber = secondNumber
    
    if  secondNumber > firstNumber :
        biggestNumber = secondNumber
        smallerNumber = firstNumber

    biggestSummer = biggestNumber
    smallerSummer = smallerNumber

    while True:
        LCM[biggestSummer] = biggestSummer

        if smallerSummer not in LCM:
            LCM[smallerSummer] = smallerSummer
        else:
            return smallerSummer

        biggestSummer += biggestNumber
        smallerSummer += smallerNumber   


if __name__ == '__main__':
    firstNumber = 789
    secondNumber = 342
    print(FindLCM(firstNumber, secondNumber))



