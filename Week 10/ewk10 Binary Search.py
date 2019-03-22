def guessGame():
    print("Let's play a game! You pick a number, and I'll guess it.")
    highest = int(input("What's the highest possible value?"))
    lowest = int(input("What's the lowest possible value?"))
    valuesdict = {}
    valuesdict['most'] = highest
    valuesdict['least'] = lowest
    done = False
    while not done:
        newrange = valuesdict['most'] - valuesdict['least']
        guess = (newrange // 2) + valuesdict['least']
        response = input("Is it {}? Type Y for yes, H for too high, and L for too low.".format(guess))
        if response == 'Y':
            done = True
            print("Hooray! I guessed it!")
        elif response == 'H':
            valuesdict['most'] = guess - 1
            print("Hmmm... Too high, eh?")
        elif response == 'L':
            valuesdict['least'] = guess + 1
            print("Darn! I thought for sure that was right!")

guessGame()