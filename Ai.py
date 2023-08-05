from Constants import Constants
import random
import math


class Ai:



    def __init__(self, numOfInputs, numOfOutputs, numOfHiddenLayers, sizeOfHiddenLayers):
        self.numOfInputs = numOfInputs
        self.numOfOutputs = numOfOutputs
        self.numOfHiddenLayers = numOfHiddenLayers
        self.sizeOfHiddenLayers = sizeOfHiddenLayers
        self.weights = []
        self.inputWeights = []
        self.hiddenWeights = []
        self.outputWeights = []

        #region++++++setting random input weights++++++
        for i in range(self.numOfInputs):
            weight = []
            for s in range(self.sizeOfHiddenLayers):
                weight.append(random.randrange(-1, 1, 0.001))

            self.inputWeights.append(weight)
        #endregion

        #region++++++setting random hidden weights+++++
        for i in range(self.numOfHiddenLayers - 1):

            columnWeights = []

            for f in range(self.sizeOfHiddenLayers):
                weight = []

                for d in range(self.sizeOfHiddenLayers):
                    weight.append(random.randrange(-1, 1, 0.001))

                columnWeights.append(weight)

            self.hiddenWeights.append(columnWeights)
        #endregion

        #region++++++setting random output weights++++++
        for i in range(self.numOfOutputs):
            weights = []

            for p in range(self.sizeOfHiddenLayers):
                weights.append(random.randrange(-1, 1, 0.001))

            self.outputWeights.append(weights)

        #endregion


        self.weights.append(self.inputWeights)
        self.weights.append(self.hiddenWeights)
        self.weights.append(self.outputWeights)


    def __gelu(x):
        return 0.5 * x * (1 + math.erf(x/math.sqrt(2)))

    #returns a list holding the values of the first hidden layer
    def __inputToFirstHiddenLayer(self, inputs: list):

        hiddenNeurons = list()

        for o in range(self.sizeOfHiddenLayers):
            nueronValue = 0

            for i in range(self.numOfInputs):
                holder = inputs[i] * self.inputWeights[o][i]
                nueronValue += holder

            nueronValue = self.__gelu(nueronValue)
            hiddenNeurons.append(nueronValue)

        return hiddenNeurons

    #the second hidden layer is column 0
    def __hiddenToHiddenLayer(self, inputs: list, endingColumn: int):

        hiddenLayer = []

        for i in range(self.sizeOfHiddenLayers):

            nueronValue = 0

            for o in range(self.sizeOfHiddenLayers):
                nueronValue += inputs[o] * self.hiddenWeights[endingColumn][o]

            nueronValue = self.__gelu(nueronValue)
            hiddenLayer.append(nueronValue)

        return hiddenLayer

    def __inputToFinalHiddenLayer(self, inputs: list):

        firstHiddenLayer = self.__inputToFirstHiddenLayer(inputs)


        for i in range(self.numOfHiddenLayers - 1):
            firstHiddenLayer = self.__hiddenToHiddenLayer(firstHiddenLayer, i)

        finalHiddenLayer = firstHiddenLayer

        return finalHiddenLayer

    def inputToOutput(self, inputs: list):

        output = []

        hiddenLayer = self.__inputToFinalHiddenLayer(inputs)

        for i in range(self.numOfOutputs):

            nueronValue = 0

            for o in range(self.sizeOfHiddenLayers):
                nueronValue += hiddenLayer[o] * self.outputWeights[i][o]

            nueronValue = self.__gelu(nueronValue)
            output.append(nueronValue)

        return output

    def __mutateWeights(self, weights: list):

        for i in range(len(weights)):

            determiningNum = random.randint(-100, 100)

            if(determiningNum > 95):
                #slightly bigger weight
                weights[i] = weights[i] * (1 + Constants.mutator)
            elif(determiningNum < -95):
                #slightly smaller weight
                weights[i] = weights[i] * (1 - Constants.mutator)

        return weights

    def meiosis(self, mom: list, dad: list):

        for i in range(self.weights):

            if(random.randint(1, 100) > 50):
                self.weights[i] = mom[i]
            else:
                self.weights[i] = dad[i]

        self.weights = self.__mutateWeights(self.weights)

        return self.weights




