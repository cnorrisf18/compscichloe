import turtle
wn=turtle.Screen()
c=turtle.Turtle()
c.color('blue')


def applyRules(leftChar):
    """ apply rule transforming leftChar to rightStr """
    rightStr = ""
    if leftChar == 'H':
        rightStr = 'HFX[+H][-H]'   # Rule 1
    elif leftChar == 'X':
        rightStr = 'X[-FFF][+FFF]FX' # Rule 2
    elif leftChar == 'F':
        rightStr = 'F[-F]F[+F]F'
    else:
        rightStr = leftChar    # no rules apply so keep the character
    return rightStr

def processString(oldStr):
    """ given a string oldStr transform it into newStr with rules """
    newStr = ""
    for ch in oldStr:
        newStr = newStr + applyRules(ch)

    return newStr


def executeLSystem(numIters,axiom):
    resultString = axiom
    for i in range(numIters):
        newString = processString(resultString)
        resultString = newString

    return resultString


import turtle

def goTurtleStep(someTurtle, someCommandChar):
    if someCommandChar == 'F':
        someTurtle.forward(50)
    elif someCommandChar == 'B':
        someTurtle.left(180)
        someTurtle.forward(50)
    elif someCommandChar == '-':
        someTurtle.left(25)
    elif someCommandChar == '+':
        someTurtle.right(25)
    elif someCommandChar == '[':
        turtleStateStack.append([someTurtle.heading(), someTurtle.xcor(), someTurtle.ycor()])
    elif someCommandChar == ']':
        (heading, x, y) = turtleStateStack.pop()
        someTurtle.setheading(heading)
        someTurtle.setposition(x, y)


def goTurtleGo(someTurtle, someCommandStr):
    for ch in someCommandStr:
        goTurtleStep(someTurtle, ch)


def buildRules(ruleString):
    ruleString.split("/n")

turtleStateStack= []


goTurtleGo(c, applyRules('F'))

wn.exitonclick()

