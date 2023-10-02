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
          self.weights = [[[0.553, 0.321, 0.751, 0.082, 0.295, 0.144, 0.925, 0.167, 0.947, 0.716, 0.941], [0.376, 0.104, 0.833, 0.953, 0.313, 0.045, 0.28, 0.646, 0.361, 0.837, 0.586], [0.907, 0.226, 0.98, 0.341, 0.708, 0.797, 0.394, 0.231, 0.182, 0.493, 0.063], [0.831, 0.243, 0.452, 0.526, 0.739, 0.801, 0.318, 0.981, 0.667, 0.26, 0.705], [0.745, 0.253, 0.696, 0.638, 0.03, 0.698, 0.969, 0.681, 0.999, 0.1, 0.899], [0.627, 0.557, 0.285, 0.101, 0.963, 0.58, 0.125, 0.364, 0.201, 0.896, 0.64], [0.512, 0.405, 0.435, 0.962, 0.881, 0.408, 0.805, 0.492, 0.587, 0.063, 0.388], [0.854, 0.939, 0.354, 0.896, 0.624, 0.363, 0.457, 0.351, 0.384, 0.431, 0.828], [0.434, 0.099, 0.24, 0.655, 0.15, 0.708, 0.052, 0.527, 0.676, 0.135, 0.336], [0.191, 0.058, 0.945, 0.336, 0.914, 0.929, 0.574, 0.289, 0.279, 0.956, 0.043], [0.145, 0.427, 0.417, 0.792, 0.33, 0.408, 0.75, 0.792, 0.746, 0.523, 0.971]], [[[0.914, 0.929, 0.908, 0.79, 0.912, 0.242, 0.583, 0.114, 0.634, 0.501, 0.757], [0.458, 0.247, 0.447, 0.807, 0.605, 0.179, 0.813, 0.873, 0.496, 0.143, 0.931], [0.402, 0.897, 0.019, 0.542, 0.788, 0.281, 0.263, 0.154, 0.948, 0.6, 0.502], [0.98, 0.868, 0.486, 0.807, 0.314, 0.662, 0.439, 0.142, 0.273, 0.593, 0.936], [0.776, 0.253, 0.912, 0.743, 0.966, 0.174, 0.268, 0.41, 0.175, 0.219, 0.453], [0.463, 0.615, 0.861, 0.372, 0.618, 0.086, 0.352, 0.944, 0.35, 0.114, 0.21], [0.123, 0.496, 0.563, 0.485, 0.907, 0.405, 0.323, 0.58, 0.807, 0.009, 0.017], [0.898, 0.512, 0.402, 0.196, 0.585, 0.482, 0.61, 0.588, 0.875, 0.031, 0.981], [0.045, 0.809, 0.839, 0.349, 0.338, 0.834, 0.902, 0.063, 0.968, 0.498, 0.363], [0.906, 0.908, 0.419, 0.873, 0.328, 0.56, 0.502, 0.949, 0.152, 0.358, 0.848], [0.652, 0.688, 0.956, 0.658, 0.678, 0.298, 0.11, 0.858, 0.186, 0.314, 0.702]], [[0.332, 0.724, 0.407, 0.337, 0.1, 0.664, 0.921, 0.466, 0.72, 0.132, 0.913], [0.827, 0.026, 0.352, 0.498, 0.626, 0.754, 0.054, 0.414, 0.865, 0.669, 0.819], [0.667, 0.084, 0.511, 0.038, 0.984, 0.655, 0.417, 0.641, 0.146, 0.733, 0.624], [0.094, 0.835, 0.939, 0.202, 0.161, 0.128, 0.119, 0.527, 0.13, 0.941, 0.712], [0.269, 0.324, 0.101, 0.051, 0.625, 0.821, 0.502, 0.334, 0.471, 0.088, 0.197], [0.771, 0.222, 0.719, 0.777, 0.648, 0.718, 0.006, 0.719, 0.784, 0.803, 0.892], [0.767, 0.16, 0.576, 0.283, 0.429, 0.727, 0.342, 0.939, 0.342, 0.64, 0.051], [0.707, 0.378, 0.518, 0.033, 0.866, 0.654, 0.211, 0.025, 0.132, 0.872, 0.458], [0.907, 0.809, 0.075, 0.766, 0.568, 0.361, 0.423, 0.916, 0.942, 0.974, 0.009], [0.407, 0.759, 0.225, 0.635, 0.267, 0.988, 0.407, 0.971, 0.463, 0.104, 0.339], [0.958, 0.5, 0.452, 0.934, 0.574, 0.922, 0.937, 0.849, 0.712, 0.298, 0.495]]], [[0.847, 0.376, 0.451, 0.743, 0.961, 0.483, 0.715, 0.733, 0.849, 0.225, 0.353]]]

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

        #logging.debug("inside __mutateWeights")

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
