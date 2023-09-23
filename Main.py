import logging
import time
from Player import Player
from Card import Card
from Constants import Constants
from Ai import Ai
import random
import os

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
printEnabled = True

def test():

    pass

roboBob = Ai(11, 1, 3, 11, False)
roboJeff = Ai(11, 1, 3, 11, False)
roboJim = Ai(11, 1, 3, 11, False)
roboSally = Ai(11, 1, 3, 11, False)
roboJoe = Ai(11, 1, 3, 11, False)
robotheHouse = Ai(11, 1, 3, 11, False)

bob = Player("bob", Constants.startingCash, 0, roboBob)
jeff = Player("jeff", Constants.startingCash, 1, roboJeff)
jim = Player("jim", Constants.startingCash, 2, roboJim)
sally = Player("sally", Constants.startingCash, 3, roboSally)
joe = Player("joe", Constants.startingCash, 4, roboJoe)
theHouse = Player("theHouse", Constants.startingCash, 5, robotheHouse)



pot = 0

isFirstBettingRound = True


dealerIndex = -1
bigBlindIndex = -2
smallBlindIndex = -3
players = list([bob, jeff, jim, sally, joe, theHouse])

#region                Making the deck

holderOne = Card(-1, -1)
holderTwo = Card(-2, -3)
holderThree = Card(-1, -5)
holderFour = Card(-1, -7)
holderFive = Card(-1, -9)

aceS = Card(1, 14)
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

aceH = Card(2, 14)
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

aceC = Card(3, 14)
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

aceD = Card(4, 14)
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

board = list((holderOne, holderTwo, holderThree, holderFour, holderFive)) #the flop, turn, and river


def betMoney(player: Player, amount):
    global pot
    amountBetted = player.betMoney(amount)
    if(amountBetted == (amount)):
        pot += amount
        return (True, amountBetted)
    else:
        pot += amountBetted
        return (False, amountBetted)

def shuffleAndResetDeck():
    global deck
    deck = [aceS, twoS, threS, fourS, fiveS, sixS, sevenS, eightS, nineS, tenS, jackS, queenS, kingS, aceH, twoH, threH, fourH, fiveH, sixH, sevenH, eightH, nineH, tenH, jackH, queenH, kingH, aceC, twoC, threC, fourC, fiveC, sixC, sevenC, eightC, nineC, tenC, jackC, queenC, kingC, aceD, twoD, threD, fourD, fiveD, sixD, sevenD, eightD, nineD, tenD, jackD, queenD, kingD]
    random.shuffle(deck)

def flop():
    for i in range(3):
        board.pop(0)
        board.append(deck.pop(0))

    if(printEnabled):
        print(f"The community cards are {board}")

def turnOrRiver():
    board.pop(0)
    board.append(deck.pop(0))
    if(printEnabled):
        print(f"The community cards are {board}")

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
    global dealerIndex, bigBlindIndex, smallBlindIndex

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
        currentBetterIndex += 1
        isFirstBettingRound = False



    while playing:
        #region                        advancing the better index and looping it around
        currentBetterIndex += 1

        if(currentBetterIndex > 5):
            currentBetterIndex = 0
        #endregion

        amountToBet = players[currentBetterIndex].getAi().inputToOutput(getInputs(players[currentBetterIndex]))[0]
        amountToBet = round(amountToBet)
        newMoneyOnTable = players[currentBetterIndex].getMoneyOnTable() + amountToBet

        if(newMoneyOnTable < getMostMoneyOnTable() and players[currentBetterIndex].isPlaying()):
            players[currentBetterIndex].setIsPlaying(False)
            if(printEnabled):
                print(f"{players[currentBetterIndex].getName()} has folded \n")




        elif(players[currentBetterIndex].isPlaying()):
            if(newMoneyOnTable == getMostMoneyOnTable()):
                players[currentBetterIndex].setHasCalled(True)

            notAllIn, amountBetted = betMoney(players[currentBetterIndex], amountToBet)

            if(not notAllIn):
                players[currentBetterIndex].setHasCalled(True)

            if(printEnabled):
                print(f"{players[currentBetterIndex].getName()} has bet ${amountBetted}")
                print(f"The pot is now at ${pot}\n")

        if(bettingIsOver()):
            playing = False

    if(printEnabled):
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

def getMostMoneyOnTable() -> int:

    mostAmountOfMoneyFromAPlayer = 0

    for player in players:
        if(player.getMoneyOnTable() > mostAmountOfMoneyFromAPlayer):
            mostAmountOfMoneyFromAPlayer = player.getMoneyOnTable()

    return mostAmountOfMoneyFromAPlayer

def getSecondMostMoneyOnTable() -> int:

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
    board = list((holderOne, holderTwo, holderThree, holderFour, holderFive))

def setup():
    shuffleAndResetDeck()
    rotateDealer()
    dealPocketCards()
    anteAndBlinds()

    if(printEnabled):
        print("\nA new round has started!")

def cleanUp():
    makeEveryonePlaying()
    clearTheBoard()
    clearPlayersHands()
    improveAi()

def getInputs(player: Player) -> list:
    inputs = list()
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
    inputs.append(player.getMoney())#value 11

    return inputs

def improveAi():

    mom = players[0]
    dad = players[1]

    for player in players:
        if(player.getMoney() > dad.getMoney()):
            dad = player
        elif(player.getMoney() > mom.getMoney()):
            mom = player

    for player in players:
        if(player.getMoney() <= 0):
            player.getAi().meiosis(mom.getAi().getWeights(), dad.getAi().getWeights())
            player.addMoney(500)
            if(printEnabled):
                print(f"{player.getName()} has run out of money and gotten a new set of weights")

def getBestPlayer() -> Player:
    dad = players[0]

    for player in players:
        if(player.getMoney() > dad.getMoney()):
            dad = player

    return dad

def findHand(player: Player) -> tuple:
    cards = list()

    availableCards = list()
    availableCards.append(player.getPocket()[0])
    availableCards.append(player.getPocket()[1])
    availableCards.append(board[0])
    availableCards.append(board[1])
    availableCards.append(board[2])
    availableCards.append(board[3])
    availableCards.append(board[4])

    #region      Finished algorithms

    #straight flush 8 and royal flush 9
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:
                    availableCards.remove(fourth)
                    for fifth in availableCards:

                        #if the hand is a straight
                        if((first.getValue() == second.getValue() + 1) and (second.getValue() == third.getValue() + 1) and (third.getValue() == fourth.getValue() + 1) and (fourth.getValue() == fifth.getValue() + 1)):

                            #if the hand if a flush
                            if((first.getSuit() == second.getSuit()) and (second.getSuit() == third.getSuit()) and (third.getSuit() == fourth.getSuit()) and (fourth.getSuit() == fifth.getSuit())):
                                cards = []
                                cards.append(first)
                                cards.append(second)
                                cards.append(third)
                                cards.append(fourth)
                                cards.append(fifth)

                                if(first.getValue() == 14):#if the start of the straight is an ace then it's a royal flush
                                    return (9, cards)
                                return (8, cards)

                    availableCards.append(fourth)
                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #four of a kind 7
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:

                    if((first.getValue() == second.getValue()) and (second.getValue() == third.getValue()) and (third.getValue() == fourth.getValue())):
                        cards = []
                        cards.append(first)
                        cards.append(second)
                        cards.append(third)
                        cards.append(fourth)
                        return (7, cards)

                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #full house 6
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:
                    availableCards.remove(fourth)
                    for fifth in availableCards:

                        if((first.getValue() == second.getValue()) and (second.getValue() == third.getValue()) and (fourth.getValue() == fifth.getValue())):
                            cards = []
                            cards.append(first)
                            cards.append(second)
                            cards.append(third)
                            cards.append(fourth)
                            cards.append(fifth)
                            return (6, cards)

                    availableCards.append(fourth)
                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #flush 5
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:
                    availableCards.remove(fourth)
                    for fifth in availableCards:

                        if((first.getSuit() == second.getSuit()) and (second.getSuit() == third.getSuit()) and (third.getSuit() == fourth.getSuit()) and (fourth.getSuit() == fifth.getSuit())):
                            cards = []
                            cards.append(first)
                            cards.append(second)
                            cards.append(third)
                            cards.append(fourth)
                            cards.append(fifth)
                            return (5, cards)

                    availableCards.append(fourth)
                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #straight 4
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:
                    availableCards.remove(fourth)
                    for fifth in availableCards:

                        if((first.getValue() == second.getValue() + 1) and (second.getValue() == third.getValue() + 1) and (third.getValue() == fourth.getValue() + 1) and (fourth.getValue() == fifth.getValue()) + 1):
                            cards = []
                            cards.append(first)
                            cards.append(second)
                            cards.append(third)
                            cards.append(fourth)
                            cards.append(fifth)
                            return (4, cards)

                    availableCards.append(fourth)
                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #three of a kind 3
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:

                if(first.getValue() == second.getValue() and second.getValue() == third.getValue()):
                    cards = []
                    cards.append(first)
                    cards.append(second)
                    cards.append(third)
                    return (3, cards)

            availableCards.append(second)
        availableCards.append(first)



    #two pair 2
    for first in availableCards:
        availableCards.remove(first)
        for second in availableCards:
            availableCards.remove(second)
            for third in availableCards:
                availableCards.remove(third)
                for fourth in availableCards:

                    if((first.getValue() == second.getValue()) and (third.getValue() == fourth.getValue())):
                        cards = []
                        cards.append(first)
                        cards.append(second)
                        cards.append(third)
                        cards.append(fourth)
                        return (2, cards)

                availableCards.append(third)
            availableCards.append(second)
        availableCards.append(first)



    #pair 1
    for first in availableCards:
        availableCards.remove(first)

        for second in availableCards:
            if(first.getValue() == second.getValue()):
                cards = []
                cards.append(first)
                cards.append(second)
                return (1, cards)
        availableCards.append(first)



    #high first 0
    highestCard = Card(-2,-2)
    for first in availableCards:
        if(first.getValue() > highestCard.getValue()):
            highestCard = first

    return (0, [highestCard])

#endregion

def findWinner() -> tuple:
    winner = players[0]
    winningHandRank = -1
    winningCards = [holderOne]

    for player in players:
        (handRank, cards) = findHand(player)

        if(player.isPlaying()):
            if(handRank > winningHandRank):
                winner = player
                winningHandRank = handRank
                winningCards = cards
            elif(handRank == winningHandRank and cards[0].getValue() > winningCards[0].getValue()):
                winner = player
                winningHandRank = handRank
                winningCards = cards
            elif(handRank == winningHandRank and cards[0].getValue() == winningCards[0].getValue() and (random.randint(0,1) > .5)):
                winner = player
                winningHandRank = handRank
                winningCards = cards

    return winner, handRank

def givePotToWinner():
    global pot
    winner, handRank = findWinner()
    winner.addMoney(pot)
    pot = 0
    if(printEnabled):
        print(f"\n\n\n\n\n\n{winner.getName()} won with a {handRank} and now has ${winner.getMoney()}")

def resetAllPlayersMoney():
    for player in players:
        player.addMoney(player.getMoney() * -1)
        player.addMoney(Constants.startingCash)




os.system('cls')


randomlyChooseDealer()

startTime = time.time()

#game loop
for i in range(1000):
    for i in range(10):
        setup()
        roundOfBetting()
        flop()
        roundOfBetting()
        turnOrRiver()#turn
        roundOfBetting()
        turnOrRiver()#river
        roundOfBetting()
        givePotToWinner()
        cleanUp()
    
    #so inflation doesn't occur
    resetAllPlayersMoney()

    with open("WeightsDump.txt", "w") as weightDump:
        weightDump.writelines(str(getBestPlayer().getAi().getWeights()))

    if(time.time() >= startTime + (Constants.timeToTrain * 60)):
        break