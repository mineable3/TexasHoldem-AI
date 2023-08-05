

class Card:

    def __init__(self,suit, inputvalue, secondvalue = None):
        self.suit = suit

        if secondvalue != None:
            self.value = (inputvalue, secondvalue)
        else:
            self.value = inputvalue

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit