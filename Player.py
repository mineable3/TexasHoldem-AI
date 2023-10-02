from Ai import Ai

class Player:

    def __init__(self, inputname: str, startingCash: int, index: int, ai: Ai):
        self.name = inputname
        self.pocket = list()#the two private cards a player holds
        self.hand = -1#the poker hand, high card = 0, pair = 1....
        self.money = startingCash
        self.moneyOnTheTable = 0
        self.__dealerbool = False
        self.__isPlaying = True
        self.__hasCalled = False
        self.index = index
        self.ai = ai

    def betMoney(self, amountToBet):
        if ((self.money - amountToBet) >= 0):
            self.money -= amountToBet
            self.moneyOnTheTable += amountToBet
            return amountToBet
        else:
            self.moneyOnTheTable += self.money
            actualAmountBetted = self.money
            self.money = 0
            return actualAmountBetted

    def addMoney(self, winnings):
        self.money += winnings

    def getMoney(self) -> int:
        return self.money + self.moneyOnTheTable

    def getMoneyOnTable(self) -> int:
        return self.moneyOnTheTable

    def resetMoneyOnTable(self):
        self.moneyOnTheTable = 0

    def addPocketCard(self, cardToAdd):
        self.pocket.append(cardToAdd)

    def setIsDealer(self, inisDealer):
        self.__dealerbool = inisDealer

    def isDealer(self):
        return self.__dealerbool

    def getPocket(self):
        return self.pocket

    def clearPocket(self):
        self.pocket = list()

    def getIndex(self):
        return self.index

    def getAi(self) -> Ai:
        return self.ai

    def isPlaying(self) -> bool:
        return self.__isPlaying

    def setIsPlaying(self, newValue):
        self.__isPlaying = newValue

    def hasCalled(self):
        return self.__hasCalled

    def setHasCalled(self, newInput):
        self.__hasCalled = newInput

    def getName(self):
        return self.name

    def setMoney(self, input):
        self.money = input
