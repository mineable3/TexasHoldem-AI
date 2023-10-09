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
          self.weights = [[[1.036, 0.602, 1.192, 0.081, 0.112, 0.118, 1.243, 0.087, 0.713, 0.775, 0.49], [0.272, 0.158, 0.404, 0.582, 0.161, 0.033, 0.356, 0.341, 0.143, 0.231, 0.201], [0.844, 0.275, 1.355, 0.107, 0.539, 1.012, 0.247, 0.292, 0.099, 0.374, 0.083], [0.719, 0.142, 0.349, 0.913, 0.69, 0.301, 0.085, 1.016, 1.193, 0.12, 1.007], [1.137, 0.158, 0.515, 0.293, 0.03, 1.375, 1.709, 0.391, 1.028, 0.099, 1.367], [0.649, 0.366, 0.655, 0.085, 2.394, 0.615, 0.119, 0.479, 0.17, 1.298, 0.583], [0.783, 0.454, 0.372, 0.612, 0.427, 0.471, 0.679, 0.392, 0.648, 0.033, 0.144], [1.365, 0.669, 0.144, 0.649, 0.382, 0.274, 0.573, 0.211, 0.406, 0.517, 0.361], [0.081, 0.056, 0.094, 0.679, 0.334, 0.483, 0.238, 1.238, 0.603, 0.054, 0.613], [0.326, 0.033, 0.68, 0.477, 0.276, 0.227, 1.012, 0.393, 0.124, 0.804, 0.033], [0.149, 0.226, 0.182, 1.002, 0.208, 0.264, 1.561, 2.029, 0.46, 0.387, 1.041]], [[[0.493, 0.821, 0.644, 0.221, 0.728, 0.191, 0.286, 0.066, 0.716, 0.307, 0.16], [0.142, 0.182, 0.43, 0.437, 0.447, 0.215, 0.681, 0.576, 0.986, 0.271, 0.876], [0.792, 0.278, 0.019, 0.388, 0.924, 0.168, 0.195, 0.327, 2.065, 1.203, 0.574], [1.194, 0.663, 0.093, 0.357, 0.103, 1.181, 0.201, 0.077, 0.295, 0.469, 0.268], [0.809, 0.185, 0.345, 0.926, 0.839, 0.213, 0.254, 0.238, 0.215, 0.117, 0.49], [1.142, 1.292, 0.487, 0.231, 0.758, 0.033, 0.144, 0.941, 0.484, 0.071, 0.099], [0.033, 0.2, 0.398, 0.173, 2.408, 0.651, 0.212, 0.205, 0.851, 0.009, 0.017], [0.487, 0.569, 0.236, 0.165, 0.896, 0.196, 0.204, 0.724, 0.451, 0.031, 0.416], [0.033, 1.26, 0.628, 0.259, 0.128, 0.807, 0.458, 0.033, 0.755, 0.124, 0.136], [1.544, 0.573, 0.296, 2.182, 0.299, 0.167, 0.182, 0.826, 0.162, 0.496, 1.156], [0.566, 0.475, 1.075, 1.535, 0.37, 0.355, 0.165, 0.603, 0.087, 0.164, 0.234]], [[0.271, 0.46, 0.192, 0.383, 0.098, 0.564, 2.042, 0.356, 0.718, 0.095, 0.736], [1.429, 0.026, 0.252, 0.342, 0.926, 0.668, 0.086, 0.486, 1.007, 0.721, 0.332], [0.316, 0.084, 0.209, 0.033, 0.811, 0.543, 0.431, 0.896, 0.115, 0.656, 0.739], [0.056, 0.552, 0.532, 0.353, 0.141, 0.077, 0.203, 0.464, 0.135, 0.623, 0.543], [0.156, 0.139, 0.033, 0.092, 0.831, 0.248, 0.271, 0.848, 0.564, 0.086, 0.455], [0.463, 0.311, 1.782, 0.802, 0.641, 0.587, 0.006, 1.024, 0.513, 0.416, 0.283], [0.582, 0.15, 0.612, 0.471, 0.128, 0.278, 0.148, 2.113, 0.283, 0.498, 0.033], [0.586, 0.151, 0.504, 0.033, 0.747, 0.242, 0.26, 0.025, 0.127, 1.484, 0.468], [0.49, 0.512, 0.064, 1.229, 0.538, 0.357, 0.361, 0.517, 1.161, 0.972, 0.009], [0.702, 0.314, 0.098, 0.536, 0.204, 0.719, 0.755, 0.687, 0.186, 0.078, 0.229], [1.417, 0.2, 0.225, 0.909, 2.321, 1.407, 1.198, 0.48, 0.388, 0.657, 0.268]]], [[0.24, 0.505, 0.443, 0.705, 1.286, 0.162, 0.269, 0.91, 0.238, 0.483, 0.095]]]
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
