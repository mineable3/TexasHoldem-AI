

class Card:

    def __init__(self,suit, inputvalue):
        self.suit = suit
        self.value = inputvalue

    def getValue(self) -> int:
        return self.value

    def getSuit(self):
        return self.suit

    def __str__(self):

        if(self.suit == 1):
            return f"{self.getValue()} of Spades"
        elif(self.suit == 2):
            return f"{self.getValue()} of Hearts"
        elif(self.suit == 3):
            return f"{self.getValue()} of Clubs"
        elif(self.suit == 4):
            return f"{self.getValue()} of Diamonds"
        elif(self.suit <= 0):
            return f"EMPTY"
        else:
            return "ERROR IN PRINTING A CARD"

    def __repr__(self):

        if(self.suit == 1):
            return f"{self.getValue()} of Spades"
        elif(self.suit == 2):
            return f"{self.getValue()} of Hearts"
        elif(self.suit == 3):
            return f"{self.getValue()} of Clubs"
        elif(self.suit == 4):
            return f"{self.getValue()} of Diamonds"
        elif(self.suit <= 0):
            return f"EMPTY"
        else:
            return "ERROR IN PRINTING A CARD"

