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
          self.weights = [[[1.019, 0.611, 1.21, 0.081, 0.108, 0.122, 1.26, 0.086, 0.702, 0.835, 0.483], [0.276, 0.162, 0.392, 0.548, 0.161, 0.033, 0.36, 0.336, 0.153, 0.238, 0.207], [0.819, 0.275, 1.295, 0.111, 0.539, 1.025, 0.228, 0.3, 0.097, 0.38, 0.084], [0.719, 0.138, 0.349, 0.873, 0.732, 0.291, 0.082, 0.971, 1.192, 0.122, 0.992], [1.038, 0.158, 0.498, 0.304, 0.03, 1.374, 1.681, 0.385, 1.107, 0.103, 1.248], [0.628, 0.382, 0.655, 0.083, 2.464, 0.597, 0.111, 0.465, 0.176, 1.355, 0.557], [0.819, 0.454, 0.366, 0.603, 0.432, 0.492, 0.709, 0.374, 0.668, 0.033, 0.146], [1.324, 0.679, 0.148, 0.649, 0.359, 0.262, 0.563, 0.208, 0.424, 0.509, 0.356], [0.082, 0.056, 0.093, 0.649, 0.334, 0.49, 0.218, 1.164, 0.594, 0.057, 0.613], [0.316, 0.033, 0.689, 0.484, 0.272, 0.23, 1.012, 0.387, 0.12, 0.828, 0.033], [0.151, 0.22, 0.179, 0.957, 0.217, 0.26, 1.606, 2.089, 0.426, 0.381, 1.089]], [[[0.492, 0.832, 0.64, 0.221, 0.694, 0.185, 0.286, 0.066, 0.716, 0.297, 0.162], [0.146, 0.182, 0.424, 0.424, 0.433, 0.212, 0.7, 0.585, 0.985, 0.263, 0.876], [0.792, 0.27, 0.019, 0.376, 0.896, 0.159, 0.201, 0.342, 2.033, 1.219, 0.601], [1.212, 0.663, 0.094, 0.356, 0.103, 1.129, 0.207, 0.077, 0.287, 0.483, 0.276], [0.833, 0.179, 0.382, 0.898, 0.826, 0.198, 0.258, 0.242, 0.212, 0.121, 0.49], [1.125, 1.35, 0.493, 0.231, 0.793, 0.033, 0.14, 0.984, 0.463, 0.072, 0.098], [0.033, 0.191, 0.386, 0.176, 2.48, 0.651, 0.221, 0.211, 0.864, 0.009, 0.017], [0.466, 0.578, 0.232, 0.161, 0.896, 0.205, 0.21, 0.67, 0.43, 0.031, 0.398], [0.033, 1.222, 0.618, 0.243, 0.122, 0.757, 0.458, 0.033, 0.744, 0.124, 0.13], [1.496, 0.6, 0.294, 2.35, 0.291, 0.166, 0.185, 0.802, 0.16, 0.543, 1.155], [0.573, 0.468, 1.042, 1.558, 0.4, 0.37, 0.164, 0.612, 0.088, 0.168, 0.233]], [[0.279, 0.439, 0.207, 0.371, 0.103, 0.581, 1.95, 0.361, 0.74, 0.094, 0.713], [1.427, 0.026, 0.24, 0.322, 0.954, 0.707, 0.089, 0.479, 1.022, 0.743, 0.342], [0.321, 0.088, 0.215, 0.033, 0.848, 0.527, 0.425, 0.937, 0.125, 0.696, 0.761], [0.06, 0.566, 0.5, 0.333, 0.139, 0.081, 0.212, 0.457, 0.133, 0.623, 0.559], [0.158, 0.149, 0.033, 0.093, 0.831, 0.268, 0.283, 0.861, 0.548, 0.086, 0.469], [0.449, 0.316, 1.864, 0.814, 0.622, 0.596, 0.006, 1.071, 0.489, 0.398, 0.303], [0.562, 0.156, 0.629, 0.492, 0.126, 0.282, 0.146, 2.018, 0.283, 0.505, 0.033], [0.551, 0.155, 0.528, 0.033, 0.747, 0.246, 0.248, 0.025, 0.125, 1.483, 0.447], [0.52, 0.528, 0.062, 1.228, 0.53, 0.341, 0.361, 0.533, 1.161, 0.972, 0.009], [0.702, 0.329, 0.094, 0.512, 0.21, 0.73, 0.755, 0.697, 0.186, 0.081, 0.235], [1.479, 0.194, 0.216, 0.893, 2.355, 1.447, 1.178, 0.48, 0.376, 0.718, 0.256]]], [[0.236, 0.476, 0.443, 0.727, 1.267, 0.168, 0.285, 0.909, 0.238, 0.469, 0.101]]]
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
