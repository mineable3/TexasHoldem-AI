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
          self.weights = [[[0.855, 0.421, 0.799, 0.093, 0.289, 0.167, 0.774, 0.15, 1.029, 0.697, 0.868], [0.382, 0.143, 0.752, 1.299, 0.278, 0.033, 0.325, 0.403, 0.311, 0.523, 0.56], [0.918, 0.359, 0.912, 0.242, 0.591, 0.581, 0.478, 0.23, 0.166, 0.635, 0.064], [0.768, 0.216, 0.517, 0.815, 0.88, 0.853, 0.243, 1.061, 0.851, 0.311, 0.868], [1.048, 0.19, 0.466, 0.586, 0.03, 0.518, 1.087, 0.744, 0.813, 0.095, 1.313], [0.864, 0.694, 0.398, 0.109, 1.362, 0.346, 0.121, 0.451, 0.14, 0.788, 0.806], [0.582, 0.478, 0.442, 0.731, 0.972, 0.403, 0.741, 0.395, 0.708, 0.075, 0.295], [0.89, 0.741, 0.465, 0.864, 0.687, 0.359, 0.442, 0.295, 0.427, 0.412, 0.983], [0.278, 0.139, 0.258, 0.957, 0.186, 0.563, 0.075, 0.706, 0.503, 0.094, 0.289], [0.2, 0.033, 0.848, 0.435, 1.045, 0.821, 0.757, 0.418, 0.224, 1.024, 0.033], [0.166, 0.388, 0.517, 1.04, 0.247, 0.434, 0.797, 1.232, 0.808, 0.533, 1.18]], [[[0.961, 1.208, 0.709, 0.525, 0.76, 0.303, 0.471, 0.083, 0.852, 0.415, 0.706], [0.361, 0.247, 0.411, 1.034, 0.472, 0.162, 0.632, 0.826, 0.512, 0.109, 1.124], [0.632, 0.875, 0.019, 0.5, 0.889, 0.331, 0.282, 0.148, 1.671, 0.484, 0.543], [1.151, 0.708, 0.51, 0.997, 0.296, 0.84, 0.348, 0.104, 0.356, 0.739, 0.581], [0.787, 0.287, 1.179, 0.95, 0.98, 0.233, 0.292, 0.473, 0.142, 0.174, 0.556], [0.4, 0.781, 0.649, 0.363, 0.447, 0.057, 0.239, 0.736, 0.36, 0.089, 0.285], [0.115, 0.587, 0.546, 0.356, 0.599, 0.417, 0.318, 0.295, 0.612, 0.009, 0.017], [0.864, 0.551, 0.308, 0.285, 0.485, 0.327, 0.289, 0.649, 0.813, 0.031, 0.766], [0.033, 0.906, 1.069, 0.423, 0.245, 1.058, 0.751, 0.042, 1.481, 0.404, 0.398], [1.003, 0.976, 0.306, 1.063, 0.281, 0.579, 0.417, 0.712, 0.142, 0.387, 1.258], [0.717, 0.655, 0.927, 0.689, 0.744, 0.395, 0.131, 0.66, 0.154, 0.197, 0.418]], [[0.307, 0.537, 0.387, 0.331, 0.113, 0.551, 1.015, 0.295, 0.89, 0.098, 0.994], [0.595, 0.026, 0.278, 0.466, 0.639, 0.618, 0.055, 0.444, 0.892, 0.591, 0.94], [0.68, 0.093, 0.509, 0.033, 0.979, 0.349, 0.558, 0.674, 0.142, 0.631, 0.622], [0.081, 0.893, 1.045, 0.189, 0.21, 0.138, 0.155, 0.449, 0.144, 1.227, 0.489], [0.28, 0.224, 0.092, 0.074, 0.975, 0.596, 0.455, 0.423, 0.391, 0.089, 0.242], [0.823, 0.177, 0.91, 0.869, 0.596, 0.731, 0.006, 1.136, 0.752, 0.864, 0.874], [0.881, 0.12, 0.741, 0.224, 0.344, 0.599, 0.338, 1.622, 0.334, 0.8, 0.039], [0.692, 0.388, 0.484, 0.033, 0.983, 0.538, 0.204, 0.025, 0.146, 0.973, 0.449], [0.798, 0.791, 0.097, 0.534, 0.667, 0.296, 0.592, 0.828, 0.973, 0.883, 0.009], [0.594, 0.66, 0.2, 0.86, 0.262, 0.722, 0.553, 0.682, 0.335, 0.099, 0.401], [1.039, 0.482, 0.26, 0.951, 0.614, 1.405, 0.869, 0.732, 0.548, 0.317, 0.432]]], [[0.679, 0.41, 0.399, 0.861, 0.888, 0.561, 0.498, 0.803, 0.708, 0.296, 0.359]]]
          self.inputWeights = self.weights[0]
          self.hiddenWeights = self.weights[1]
          self.outputWeights = self.weights[2]

        else:
            #region++++++setting random input weights++++++
            for i in range(self.numOfInputs):
                weight = []
                for s in range(self.sizeOfHiddenLayers):
                    weight.append(round(random.random(), Constants.precisionOfWeights))

                self.inputWeights.append(weight)
            #endregion

            #region++++++setting random hidden weights+++++
            for i in range(self.numOfHiddenLayers - 1):

                columnWeights = []

                for f in range(self.sizeOfHiddenLayers):
                    weight = []

                    for d in range(self.sizeOfHiddenLayers):
                        weight.append(round(random.random(), Constants.precisionOfWeights))

                    columnWeights.append(weight)

                self.hiddenWeights.append(columnWeights)
            #endregion

            #region++++++setting random output weights++++++
            for i in range(self.numOfOutputs):
                weight = []
                for p in range(self.sizeOfHiddenLayers):
                    weight.append(round(random.random(), Constants.precisionOfWeights))


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
            output.append(round(value * scalingFactor, Constants.outputPrecicion))

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

        output = self.__scaleAndRoundList(output, Constants.outputScaleFactor)

        return output

    def __mutateWeights(self, weights: list):

        #input layer
        for i in range(len(weights[0])):
            for o in range(len(weights[0][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight
                    #logging.debug(weights[0][i][o])
                    weights[0][i][o] = round(weights[0][i][o] * (1 + Constants.factorOfMutation), Constants.precisionOfWeights)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    #logging.debug(weights[0][i][o])
                    weights[0][i][o] = round(weights[0][i][o] * (1 - Constants.factorOfMutation), Constants.precisionOfWeights)

        #hidden layers
        for i in range(len(weights[1])):
            for o in range(len(weights[1][i])):
                for u in range(len(weights[1][i][o])):
                    determiningNum = random.randint(-100, 100)

                    if(determiningNum > 95):
                        #slightly bigger weight
                        weights[1][i][o][u] = round(weights[1][i][o][u] * (1 + Constants.factorOfMutation), Constants.precisionOfWeights)
                    elif(determiningNum < -95):
                        #slightly smaller weight
                        weights[1][i][o][u] = round(weights[1][i][o][u] * (1 - Constants.factorOfMutation), Constants.precisionOfWeights)

        #output layer
        for i in range(len(weights[2])):
            for o in range(len(weights[2][i])):
                determiningNum = random.randint(-100, 100)

                if(determiningNum > 95):
                    #slightly bigger weight
                    weights[2][i][o] = round(weights[2][i][o] * (1 + Constants.factorOfMutation), Constants.precisionOfWeights)
                elif(determiningNum < -95):
                    #slightly smaller weight
                    weights[2][i][o] = round(weights[2][i][o] * (1 - Constants.factorOfMutation), Constants.precisionOfWeights)

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
