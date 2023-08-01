def GuessIsLCM(firstNumber, secondNumber, guess):
    LCM = {}
    biggestNumber = firstNumber
    smallerNumber = secondNumber
    
    if  secondNumber > firstNumber :
        biggestNumber = secondNumber
        smallerNumber = firstNumber

    biggestSummer = biggestNumber
    smallerSummer = smallerNumber

    while smallerSummer  <= guess:
        LCM[biggestSummer] = biggestSummer

        if smallerSummer not in LCM:
            LCM[smallerSummer] = smallerSummer
        elif smallerSummer in LCM and smallerSummer == guess:
            return True
        else:
            return False

        biggestSummer += biggestNumber
        smallerSummer += smallerNumber

    return False       

def MultiplesUntilLCM(number, LCM):
    summer = number
    multiples = ""
    while summer != LCM:
        multiples += (str(summer) + ', ')
        summer += number
    multiples += str(summer)
    return multiples

if __name__ == '__main__':
    firstNumber = input("Enter your first number:\n")
    while not firstNumber.isdigit():
        print("Value entered is not an integer.")
        firstNumber = input("Enter your first number:\n")
    firstNumber = int(firstNumber)

    secondNumber = input("Enter your second number:\n")
    while not secondNumber.isdigit():
        print("Value entered is not an integer.")
        secondNumber = input("Enter your second number:\n")
    secondNumber = int(secondNumber)   

    guess = input("Enter your guess:\n")
    while not guess.isdigit():
        print("Value entered is not an integer.")
        guess = input("Enter your guess:\n")
    guess = int(guess)

    if GuessIsLCM(firstNumber, secondNumber, guess):
        print(MultiplesUntilLCM(firstNumber, guess))
        print(MultiplesUntilLCM(secondNumber, guess))
    else:
        print("Guess is not LCM.")
    



