import logging
from Constants import Constants
import random
import math

class Ai:

    def __init__(self, numOfInputs, numOfOutputs, numOfHiddenLayers, sizeOfHiddenLayers, randomWeights: bool):
        self.numOfInputs = numOfInputs
        self.numOfOutputs = numOfOutputs
        self.numOfHiddenLayers = numOfHiddenLayers
        self.sizeOfHiddenLayers = sizeOfHiddenLayers
        self.weights = []
        self.inputWeights = []
        self.hiddenWeights = []
        self.outputWeights = []

        if(randomWeights == False):
          self.weights = [[[1.051, 0.629, 1.192, 0.081, 0.112, 0.118, 1.224, 0.087, 0.713, 0.823, 0.49], [0.276, 0.158, 0.386, 0.556, 0.161, 0.033, 0.371, 0.346, 0.145, 0.231, 0.198], [0.844, 0.283, 1.315, 0.109, 0.531, 1.011, 0.239, 0.292, 0.1, 0.368, 0.083], [0.719, 0.138, 0.364, 0.86, 0.71, 0.295, 0.082, 0.971, 1.174, 0.12, 0.977], [1.054, 0.16, 0.506, 0.301, 0.03, 1.396, 1.681, 0.385, 1.107, 0.1, 1.267], [0.639, 0.37, 0.665, 0.085, 2.429, 0.597, 0.115, 0.458, 0.173, 1.315, 0.574], [0.807, 0.447, 0.366, 0.603, 0.421, 0.471, 0.689, 0.386, 0.668, 0.033, 0.144], [1.365, 0.689, 0.146, 0.649, 0.37, 0.262, 0.572, 0.211, 0.412, 0.501, 0.351], [0.082, 0.055, 0.093, 0.669, 0.344, 0.49, 0.218, 1.219, 0.603, 0.058, 0.613], [0.316, 0.033, 0.71, 0.484, 0.272, 0.224, 0.982, 0.399, 0.12, 0.804, 0.033], [0.151, 0.229, 0.185, 0.943, 0.214, 0.26, 1.584, 2.059, 0.432, 0.387, 1.089]], [[[0.492, 0.833, 0.641, 0.224, 0.705, 0.185, 0.286, 0.068, 0.727, 0.297, 0.16], [0.146, 0.182, 0.424, 0.412, 0.433, 0.218, 0.69, 0.576, 0.928, 0.263, 0.863], [0.78, 0.278, 0.019, 0.376, 0.91, 0.168, 0.201, 0.337, 2.033, 1.22, 0.592], [1.23, 0.653, 0.094, 0.362, 0.107, 1.181, 0.207, 0.077, 0.291, 0.476, 0.276], [0.821, 0.185, 0.365, 0.898, 0.839, 0.207, 0.258, 0.242, 0.218, 0.117, 0.49], [1.142, 1.35, 0.48, 0.231, 0.781, 0.033, 0.144, 0.955, 0.463, 0.07, 0.098], [0.033, 0.197, 0.38, 0.17, 2.407, 0.651, 0.218, 0.214, 0.838, 0.009, 0.017], [0.473, 0.587, 0.236, 0.163, 0.883, 0.199, 0.207, 0.701, 0.444, 0.031, 0.404], [0.033, 1.241, 0.618, 0.247, 0.128, 0.759, 0.451, 0.033, 0.733, 0.122, 0.128], [1.52, 0.591, 0.295, 2.315, 0.287, 0.166, 0.182, 0.814, 0.158, 0.519, 1.155], [0.582, 0.482, 1.043, 1.512, 0.382, 0.36, 0.167, 0.612, 0.086, 0.166, 0.233]], [[0.267, 0.453, 0.204, 0.371, 0.101, 0.548, 1.98, 0.346, 0.74, 0.096, 0.714], [1.45, 0.026, 0.244, 0.332, 0.954, 0.718, 0.088, 0.486, 1.007, 0.754, 0.337], [0.326, 0.086, 0.218, 0.033, 0.811, 0.535, 0.431, 0.951, 0.123, 0.696, 0.75], [0.057, 0.558, 0.516, 0.338, 0.137, 0.078, 0.206, 0.464, 0.133, 0.605, 0.543], [0.156, 0.145, 0.033, 0.095, 0.831, 0.264, 0.279, 0.887, 0.556, 0.086, 0.469], [0.449, 0.321, 1.836, 0.814, 0.613, 0.587, 0.006, 1.039, 0.496, 0.41, 0.295], [0.572, 0.15, 0.639, 0.485, 0.126, 0.282, 0.146, 2.018, 0.287, 0.498, 0.033], [0.595, 0.153, 0.528, 0.033, 0.758, 0.25, 0.252, 0.025, 0.125, 1.483, 0.468], [0.504, 0.536, 0.061, 1.229, 0.53, 0.356, 0.356, 0.533, 1.127, 0.987, 0.009], [0.724, 0.319, 0.094, 0.52, 0.204, 0.741, 0.733, 0.677, 0.183, 0.079, 0.235], [1.415, 0.203, 0.213, 0.908, 2.391, 1.428, 1.251, 0.473, 0.388, 0.697, 0.26]]], [[0.236, 0.49, 0.45, 0.716, 1.267, 0.16, 0.269, 0.937, 0.234, 0.462, 0.098]]]
          self.inputWeights = self.weights[0]
          self.hiddenWeights = self.weights[1]
          self.outputWeights = self.weights[2]

        else:
            #region++++++setting random input weights++++++
            for i in range(self.numOfInputs):
                weight = []
                for s in range(self.sizeOfHiddenLayers):
                    weight.append(round(random.random(), Constants.PRECISION_OF_WEIGHTS))

                self.inputWeights.append(weight)
            #endregion

            #region++++++setting random hidden weights+++++
            for i in range(self.numOfHiddenLayers - 1):

                columnWeights = []

                for f in range(self.sizeOfHiddenLayers):
                    weight = []

                    for d in range(self.sizeOfHiddenLayers):
                        weight.append(round(random.random(), Constants.PRECISION_OF_WEIGHTS))

                    columnWeights.append(weight)

                self.hiddenWeights.append(columnWeights)
            #endregion

            #region++++++setting random output weights++++++
            for i in range(self.numOfOutputs):
                weight = []
                for p in range(self.sizeOfHiddenLayers):
                    weight.append(round(random.random(), Constants.PRECISION_OF_WEIGHTS))


                self.outputWeights.append(weight)
            #endregion


            self.weights.append(self.inputWeights)
            self.weights.append(self.hiddenWeights)
            self.weights.append(self.outputWeights)

    def __gelu(self, value) -> float:
        return 0.5 * value * (1 + math.erf(value/math.sqrt(2)))

    def __scaleAndRoundList(self, inputList: list, scalingFactor: int):

        output = list()

        for value in inputList:
            output.append(round(value * scalingFactor, Constants.OUTPUT_PRECISION))

        return output

    #returns a list holding the values of the first hidden layer
    def __inputToFirstHiddenLayer(self, inputs: list):

        hiddenNeurons = list()

        for o in range(self.sizeOfHiddenLayers):
            nueronValue = int(0)

            for i in range(self.numOfInputs):
                #logging.debug(self.inputWeights[o][i])
                #logging.debug(inputs[i])
                #logging.debug(inputs[i] * self.inputWeights[o][i])
                holder = inputs[i] * self.inputWeights[o][i]
                #logging.debug(holder)
                #logging.debug(type(holder))
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

        output = self.__scaleAndRoundList(output, Constants.OUTPUT_SCALE_FACTOR)

        return output

    def __mutateWeights(self, weights: list):

        #input layer
        for i in range(len(weights[0])):
            for o in range(len(weights[0][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight
                    #logging.debug(weights[0][i][o])
                    weights[0][i][o] = round(weights[0][i][o] * (1 + Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    #logging.debug(weights[0][i][o])
                    weights[0][i][o] = round(weights[0][i][o] * (1 - Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)

        #hidden layers
        for i in range(len(weights[1])):
            for o in range(len(weights[1][i])):
                for u in range(len(weights[1][i][o])):
                    determiningNum = random.randint(-100, 100)

                    if(determiningNum > 95):
                        #slightly bigger weight
                        weights[1][i][o][u] = round(weights[1][i][o][u] * (1 + Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)
                    elif(determiningNum < -95):
                        #slightly smaller weight
                        weights[1][i][o][u] = round(weights[1][i][o][u] * (1 - Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)

        #output layer
        for i in range(len(weights[2])):
            for o in range(len(weights[2][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight
                    weights[2][i][o] = round(weights[2][i][o] * (1 + Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    weights[2][i][o] = round(weights[2][i][o] * (1 - Constants.FACTOR_OF_MUTATION), Constants.PRECISION_OF_WEIGHTS)

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
