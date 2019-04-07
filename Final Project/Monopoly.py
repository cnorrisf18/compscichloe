import turtle
import random

#(GASP) Global variables! That are needed for multiple functions...
player = turtle.Turtle()
comp1 = turtle.Turtle()
comp2 = turtle.Turtle()
comp3 = turtle.Turtle()
comchest = turtle.Turtle()
chance = turtle.Turtle()

def getPos(x, y):
    print("(",x , y,")")
    return
def drawBoard(playercolor):
    #set background image
    board=turtle.Screen()
    board.setup(700, 700, None, None)
    board.bgpic("board.gif")
    #draw community chest and chance
    comchest.color("darkblue")
    comchest.penup()
    comchest.begin_fill()
    comchest.setpos(-227, 133)
    comchest.pendown()
    comchest.setpos(-157, 62)
    comchest.setpos(-56, 159)
    comchest.setpos(-128, 229)
    comchest.setpos(-227, 133)
    comchest.end_fill()
    chance.color("lightgreen")
    chance.penup()
    chance.begin_fill()
    chance.setpos(128, -231)
    chance.pendown()
    chance.setpos(229, -135)
    chance.setpos(155, -64)
    chance.setpos(57, -164)
    chance.setpos(128, -231)
    chance.end_fill()
    #set up players
    player.shape("turtle")
    player.color(playercolor)
    player.penup()
    player.setpos(267, -272)
    player.pendown()
    comp1.shape("arrow")
    comp1.color("red")
    comp1.penup()
    comp1.setpos(322, -270)
    comp1.pendown()
    comp2.shape("circle")
    comp2.color("blue")
    comp2.penup()
    comp2.setpos(268, -313)
    comp2.pendown()
    comp3.shape("square")
    comp3.color("yellow")
    comp3.penup()
    comp3.setpos(326, -320)
    comp3.pendown()
    #coord testing (will be removed eventually)
    board.onscreenclick(getPos)
    board.mainloop()
    

class Tiles:
    """
    Head Space for Tiles
    Properties:
    Can be owned/not owned/can't be owned
    Can contain player pieces/be empty
    Has a price/doesn't have a price

    Methods:
    Land on it
    Leave it
    Buy it
    Sell it
    """
class Locations(Tiles):
    """
    Head Space for Locations

    Properties:
    all properties of Tiles
        -can be owned/not owned
        -each one has a specific, unique buy price
    each one has other locations that it pairs with/can form a monopoly with
    can be part of a monopoly
    has rent prices
    has sell prices
    has mortgage price(? might not do this)
    can have houses or hotels on them, each with their own price

    Methods:
    all methods of Tiles
    ask player if they want to buy it if they land on it while it's unowned
    charge players rent if they land on it while it's owned
    if owner looses, property becomes unowned
    registers when it becomes a monopoly
    registers when it looses monopoly
    registers owner, or lack of owner
    houses and hotels can be bought and sold from the property if it is part of a monopoly
    """

class Utilities(Tiles):
    """
    Head space for Utilities
    Properties:
    all properties of Tiles
        -can be owned/not owned
        -each one has a unique price
    there are only 2 utilities
    have special rent prices (4 * dice roll for 1 owned, 10 * dice roll for 2 owned)
    has sell prices
    has mortgage prices(?)

    Methods:
    all methods of Tiles
    ask player if they want to buy it if they land on it while it's unowned
    charge players rent if they land on it while it's owned
    if owner looses, property becomes unowned
    registers when both are owned by the same person
    registers when owner looses a one
    registers owner, or lack of owner
    """
class Railroads(Tiles):
    """
    Head space for Railroads
    Properties:
    all properties of Tiles
    has different rent based on how many railroads are owned
    4 railroads
    has sell prices
    has mortgage prices(?)

    Methods:
    all methods of Tiles
    ask player if they want to buy it if they land on it while it's unowned
    charge players rent if they land on it while it's owned
    if owner looses, property becomes unowned
    registers how many are owned/player
    registers when owner looses one
    registers owner, or lack of owner
    """
class ChanceChest(Tiles):
    """
    Head space for ChanceChest
    Properties:
    all properties of Tiles
        -can't be owned
        -contain a certain amount of cards based on what has been played
        -does not have rent
    Methods:
    all methods of Tiles
    different cards proc when space is landed on by a player
    """
class Tax(Tiles):
    """
    Head spae for ChanceChest
    Properties:
    all properties of Tiles
    """
class Jail(Tiles):
    4
class GotoJail(Tiles):
    3
class FreeParking(Tiles):
    3
class Go(Tiles):
    3


def mainGame():
    print("Welcome to Monopoly! Today you will be playing against 3 computer characters. Enjoy!")
    print("You are the turtle-shaped character.")
    pcolor = input("First, what color would you like to be? Choose wisely! :D")
    print("Gotcha. Good choice! Now we'll set up the board...")
    drawBoard(pcolor)
mainGame()