from Player import Player
from Card import Card
from Constants import Constants
from Ai import Ai
import random
import os


def test():


    pass



bob = Player("bob", Constants.startingCash, 0)
jeff = Player("jeff", Constants.startingCash, 1)
jim = Player("jim", Constants.startingCash, 2)
sally = Player("sally", Constants.startingCash, 3)
joe = Player("joe", Constants.startingCash, 4)
house = Player("house", Constants.startingCash, 5)

roboBob = Ai(22, 1, 2, 11)
roboJeff = Ai(22, 1, 2, 11)
roboJim = Ai(22, 1, 2, 11)
roboSally = Ai(22, 1, 2, 11)
roboJoe = Ai(22, 1, 2, 11)
roboHouse = Ai(22, 1, 2, 11)

pot = 0

board = list() #the flop, turn, and river

dealerIndex = -1
bigBlindIndex = -2
smallBlindIndex = -3
players = list([bob, jeff, jim, sally, joe, house])

#region                Making the deck
aceS = Card(1, 1, 14)
twoS = Card(1, 2)
threS= Card(1, 3)
fourS = Card(1, 4)
fiveS = Card(1, 5)
sixS = Card(1, 6)
sevenS = Card(1, 7)
eightS = Card(1, 8)
nineS = Card(1, 9)
tenS = Card(1, 10)
jackS = Card(1, 11)
queenS = Card(1, 12)
kingS = Card(1, 13)

aceH = Card(2, 1, 14)
twoH = Card(2, 2)
threH= Card(2, 3)
fourH = Card(2, 4)
fiveH = Card(2, 5)
sixH = Card(2, 6)
sevenH = Card(2, 7)
eightH = Card(2, 8)
nineH = Card(2, 9)
tenH = Card(2, 10)
jackH = Card(2, 11)
queenH = Card(2, 12)
kingH = Card(2, 13)

aceC = Card(3, 1, 14)
twoC = Card(3, 2)
threC= Card(3, 3)
fourC = Card(3, 4)
fiveC = Card(3, 5)
sixC = Card(3, 6)
sevenC = Card(3, 7)
eightC = Card(3, 8)
nineC = Card(3, 9)
tenC = Card(3, 10)
jackC = Card(3, 11)
queenC = Card(3, 12)
kingC = Card(3, 13)

aceD = Card(4, 1, 14)
twoD = Card(4, 2)
threD= Card(4, 3)
fourD = Card(4, 4)
fiveD = Card(4, 5)
sixD = Card(4, 6)
sevenD = Card(4, 7)
eightD = Card(4, 8)
nineD = Card(4, 9)
tenD = Card(4, 10)
jackD = Card(4, 11)
queenD = Card(4, 12)
kingD = Card(4, 13)


deck = [aceS, twoS, threS, fourS, fiveS, sixS, sevenS, eightS, nineS, tenS, jackS, queenS, kingS, aceH, twoH, threH, fourH, fiveH, sixH, sevenH, eightH, nineH, tenH, jackH, queenH, kingH, aceC, twoC, threC, fourC, fiveC, sixC, sevenC, eightC, nineC, tenC, jackC, queenC, kingC, aceD, twoD, threD, fourD, fiveD, sixD, sevenD, eightD, nineD, tenD, jackD, queenD, kingD]

#endregion

def betMoney(player, amount):
    global pot
    amountBetted = player.betMoney(amount)
    if(amountBetted == (amount)):
        pot += amount
        return True
    else:
        pot += amountBetted
        return False

def allIn(player):
    betMoney(player, player.getMoney())

def shuffleDeck():
    random.shuffle(deck)

def flop():
    for i in range(3):
        board.append(deck.pop(0))

def turnOrRiver():
    board.append(deck.pop(0))

def dealPocketCards():
    for i in range(len(players)):
        players[i].addPocketCard(deck.pop(0))

    for i in range(len(players)):
        players[i].addPocketCard(deck.pop(0))

def chooseDealer():
    global dealerIndex, bigBlindIndex, smallBlindIndex
    dealerIndex = random.randint(0, 5)

    if(dealerIndex == 5):
        bigBlindIndex = 0
    else:
        bigBlindIndex = dealerIndex + 1

    if(bigBlindIndex == 5):
        smallBlindIndex = 0
    else:
        smallBlindIndex = bigBlindIndex + 1

def rotateDealer():
    global dealerIndex

    if(dealerIndex == 5):
        dealerIndex = 0
    else:
        dealerIndex += 1
    
    if(bigBlindIndex == 5):
        bigBlindIndex = 0
    else:
        bigBlindIndex += 1

    if(smallBlindIndex == 5):
        smallBlindIndex = 0
    else:
        smallBlindIndex += 1

def anteAndBlinds():
    for i in range(len(players)):
        betMoney(players[i], Constants.ante)

    betMoney(players[bigBlindIndex], Constants.bigBlind - Constants.ante)
    betMoney(players[smallBlindIndex], (Constants.bigBlind / 2) - Constants.ante)

def setup():
    shuffleDeck()
    chooseDealer()
    dealPocketCards()

def getInputs(player: Player):
    inputs = []
    inputs.append(player.getPocket()[0].getValue())
    inputs.append(player.getPocket()[1].getValue())
    inputs.append(board[0].getValue())
    inputs.append(board[1].getValue())
    inputs.append(board[2].getValue())
    inputs.append(board[3].getValue())
    inputs.append(board[4].getValue())
    inputs.append(pot)
    #inputs.append(minimumBetToKeepPlaying)
    #inputs.append(playersStilBetting)
    inputs.append(players[0].getMoneyOnTable())
    inputs.append(players[1].getMoneyOnTable())
    inputs.append(players[2].getMoneyOnTable())
    inputs.append(players[3].getMoneyOnTable())
    inputs.append(players[4].getMoneyOnTable())
    inputs.append(players[5].getMoneyOnTable())
    inputs.append(players[0].getMoney())
    inputs.append(players[1].getMoney())
    inputs.append(players[2].getMoney())
    inputs.append(players[3].getMoney())
    inputs.append(players[4].getMoney())
    inputs.append(players[5].getMoney())


test()

setup()

#game loop
for i in range(100):
    pass


for i in range(1):
    os.system("cls")