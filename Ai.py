import logging
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
                weight.append(round(random.random(), 3))

            self.inputWeights.append(weight)
        #endregion

        #region++++++setting random hidden weights+++++
        for i in range(self.numOfHiddenLayers - 1):

            columnWeights = []

            for f in range(self.sizeOfHiddenLayers):
                weight = []

                for d in range(self.sizeOfHiddenLayers):
                    weight.append(round(random.random(), 3))

                columnWeights.append(weight)

            self.hiddenWeights.append(columnWeights)
        #endregion

        #region++++++setting random output weights++++++
        for i in range(self.numOfOutputs):
            weights = []
            for p in range(self.sizeOfHiddenLayers):
                weight.append(round(random.random(), 3))


            self.outputWeights.append(weight)
        #endregion


        self.weights.append(self.inputWeights)
        self.weights.append(self.hiddenWeights)
        self.weights.append(self.outputWeights)


    def __gelu(self, value) -> float:
        return 0.5 * value * (1 + math.erf(value/math.sqrt(2)))

    #returns a list holding the values of the first hidden layer
    def __inputToFirstHiddenLayer(self, inputs: list):

        hiddenNeurons = list()

        for o in range(self.sizeOfHiddenLayers):
            nueronValue = int(0)

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
                nueronValue += inputs[o] * self.hiddenWeights[endingColumn][i][o]

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

        #input layer
        for i in range(len(weights[0])):
            for o in range(len(weights[0][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight

                    weights[0][i][o] = weights[0][i][o] * (1 + Constants.factorOfMutation)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    weights[0][i][o] = weights[0][i][o] * (1 - Constants.factorOfMutation)

        #hidden layers
        for i in range(len(weights[1])):
            for o in range(len(weights[1][i])):
                for u in range(len(weights[1][i][o])):
                    determiningNum = random.randint(-100, 100)

                    if(determiningNum > 95):
                        #slightly bigger weight
                        weights[1][i][o][u] = weights[1][i][o][u] * (1 + Constants.factorOfMutation)
                    elif(determiningNum < -95):
                        #slightly smaller weight
                        weights[1][i][o][u] = weights[1][i][o][u] * (1 - Constants.factorOfMutation)

        #output layer
        for i in range(len(weights[2])):
            for o in range(len(weights[2][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight
                    weights[2][i][o] = weights[2][i][o] * (1 + Constants.factorOfMutation)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    weights[2][i][o] = weights[2][i][o] * (1 - Constants.factorOfMutation)

        return weights

    def meiosis(self, mom: list, dad: list):

        #input layer
        for i,value in enumerate(self.weights[0]):

            if(random.randint(1, 100) > 50):
                value = mom[0][i]
            else:
                value = dad[0][i]
            self.weights[0][i] = value

        #hidden layers
        for i,array in enumerate(self.weights[1]):
            for o,value in enumerate(array):

                if(random.randint(1, 100) > 50):
                    value = mom[1][i][o]
                else:
                    value = dad[1][i][o]
                self.weights[1][i][o] = value

        #output layer
        for i,value in enumerate(self.weights[2]):

            if(random.randint(1, 100) > 50):
                value = mom[2][i]
            else:
                value = dad[2][i]
            self.weights[2][i] = value

        self.weights = self.__mutateWeights(self.weights)

        return self.weights

    def getWeights(self):
        return self.weights



