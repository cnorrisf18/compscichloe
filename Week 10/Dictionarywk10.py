def fruitDictInput():
    done=False
    fruitDict={}
    while not done:
        fruit=input("Enter a fruit. If done, press enter.")
        if fruit == "":
            done=True
        else:
            print("You entered: ", fruit)
            if fruit not in fruitDict:
                fruitDict[fruit] = 0
            fruitDict[fruit] = fruitDict[fruit] + 1
    for fruits in fruitDict:
        print("You entered ", fruitDict[fruits], fruits)
    return fruitDict

fruitDictInput()
