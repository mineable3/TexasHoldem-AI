from Player import Player
from Card import Card
from Constants import Constants
from Ai import Ai
import random
import os


def test():


    pass

roboBob = Ai(11, 1, 3, 11)
roboJeff = Ai(11, 1, 3, 11)
roboJim = Ai(11, 1, 3, 11)
roboSally = Ai(11, 1, 3, 11)
roboJoe = Ai(11, 1, 3, 11)
roboHouse = Ai(11, 1, 3, 11)

bob = Player("bob", Constants.startingCash, 0, roboBob)
jeff = Player("jeff", Constants.startingCash, 1, roboJeff)
jim = Player("jim", Constants.startingCash, 2, roboJim)
sally = Player("sally", Constants.startingCash, 3, roboSally)
joe = Player("joe", Constants.startingCash, 4, roboJoe)
house = Player("house", Constants.startingCash, 5, roboHouse)



pot = 0

isFirstBettingRound = True

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

def shuffleAndResetDeck():
    deck = [aceS, twoS, threS, fourS, fiveS, sixS, sevenS, eightS, nineS, tenS, jackS, queenS, kingS, aceH, twoH, threH, fourH, fiveH, sixH, sevenH, eightH, nineH, tenH, jackH, queenH, kingH, aceC, twoC, threC, fourC, fiveC, sixC, sevenC, eightC, nineC, tenC, jackC, queenC, kingC, aceD, twoD, threD, fourD, fiveD, sixD, sevenD, eightD, nineD, tenD, jackD, queenD, kingD]
    random.shuffle(deck)

def flop():
    for i in range(3):
        board.append(deck.pop(0))

    print(f"The community card are {board}")

def turnOrRiver():
    board.append(deck.pop(0))
    print(f"The community card are {board}")

def dealPocketCards():
    for i in range(len(players)):
        players[i].addPocketCard(deck.pop(0))

    for i in range(len(players)):
        players[i].addPocketCard(deck.pop(0))

def randomlyChooseDealer():
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

def roundOfBetting():
    global dealerIndex
    global isFirstBettingRound

    playing = True
    resetWhoHasCalled()

    currentBetterIndex = dealerIndex

    if (isFirstBettingRound):
        currentBetterIndex -= 2
        isFirstBettingRound = False



    while playing:
        #region                        advancing the better index and looping it around
        currentBetterIndex -= 1

        if(currentBetterIndex < 0):
            currentBetterIndex = 5
        #endregion

        amountToBet = players[currentBetterIndex].getAi().inputToOutput(getInputs(players[currentBetterIndex]))
        newMoneyOnTable = players[currentBetterIndex].getMoneyOnTable() + amountToBet

        if(newMoneyOnTable < getMostMoneyOnTable()):
            players[currentBetterIndex].setIsPlaying(False)
            print(f"{players[currentBetterIndex].getName()} has folded")




        elif(players[currentBetterIndex].isPlaying()):
            if(newMoneyOnTable == getMostMoneyOnTable()):
                players[currentBetterIndex].setHasCalled(True)

            betMoney(players[currentBetterIndex], amountToBet)
            print(f"{players[currentBetterIndex].getName()} has bet ${amountToBet}")

        if(bettingIsOver()):
            playing = False

    print("This round of betting is over!")

def makeEveryonePlaying():
    for player in players:
        player.setIsPlaying(True)

def resetWhoHasCalled():
    for player in players:
        player.setHasCalled(False)

def bettingIsOver():

    #finding all the players currently betting
    currentBetters = list()
    for player in players:
        if(player.isPlaying()):
            currentBetters.append(player)


    numOfPlayersThatCalled = 0
    for player in currentBetters:
        if(player.hasCalled()):
            numOfPlayersThatCalled += 1
    
    if(len(currentBetters) == numOfPlayersThatCalled):
        return True
    else:
        return False

def getMostMoneyOnTable():

    mostAmountOfMoneyFromAPlayer = 0

    for player in players:
        if(player.getMoneyOnTable() > mostAmountOfMoneyFromAPlayer):
            mostAmountOfMoneyFromAPlayer = player.getMoneyOnTable()

    return mostAmountOfMoneyFromAPlayer

def getSecondMostMoneyOnTable():

    mostAmountOfMoneyFromAPlayer = 0

    for player in players:
        if((player.getMoneyOnTable() > mostAmountOfMoneyFromAPlayer) and (player.getMoneyOnTable() != getMostMoneyOnTable())):
            mostAmountOfMoneyFromAPlayer = player.getMoneyOnTable()

    return mostAmountOfMoneyFromAPlayer

def clearPlayersHands():
    for player in players:
        player.clearPocket()

def clearTheBoard():
    global board
    board = list()

def setup():
    makeEveryonePlaying()
    clearTheBoard()
    clearPlayersHands()
    shuffleAndResetDeck()
    randomlyChooseDealer()
    dealPocketCards()
    anteAndBlinds()

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
    inputs.append(getMostMoneyOnTable())
    inputs.append(player.getMoneyOnTable())
    inputs.append(player.getMoney())

def improveAi():

    mom = None
    dad = None

    mostMoney = getMostMoneyOnTable()
    secondMostMoney = getSecondMostMoneyOnTable()

    for player in players:
        if(player.getMoneyOnTable() == mostMoney):
            dad = player
        if(player.getMoneyOnTable() == secondMostMoney):
            mom = player

    for player in players:
        if(player.getMoney() <= 0):
            player.getAi.meiosis(mom.getAi().getWeights(), dad.getAi().getWeights())
            print(f"{player.getName()} has run out of money and gotten a new set of weights")


test()


#game loop
for i in range(10):
    setup()
    roundOfBetting()
    flop()
    roundOfBetting()
    turnOrRiver()#turn
    roundOfBetting()
    turnOrRiver()#river
    roundOfBetting()