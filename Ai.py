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
          self.weights = [[[1.03404, 0.57232, 1.22146, 0.07741, 0.10748, 0.1154, 1.25962, 0.08511, 0.65979, 0.8222, 0.48516], [0.27312, 0.16129, 0.36896, 0.52109, 0.15773, 0.03436, 0.37638, 0.34434, 0.14987, 0.23686, 0.20784], [0.76705, 0.28175, 1.25563, 0.12009, 0.52546, 0.99429, 0.22563, 0.29344, 0.09224, 0.39333, 0.08273], [0.74376, 0.14215, 0.32383, 0.85595, 0.75346, 0.28364, 0.07567, 0.95602, 1.19728, 0.12131, 0.97178], [1.0274, 0.15789, 0.51284, 0.30041, 0.03088, 1.40835, 1.63059, 0.38879, 1.06312, 0.10342, 1.198], [0.64327, 0.39544, 0.65787, 0.08638, 2.50028, 0.59076, 0.10608, 0.48374, 0.17338, 1.29484, 0.57151], [0.86491, 0.4717, 0.37886, 0.59078, 0.40239, 0.482, 0.68416, 0.41107, 0.69147, 0.03317, 0.14274], [1.37668, 0.662, 0.14282, 0.64874, 0.34977, 0.27284, 0.55744, 0.21318, 0.41321, 0.47717, 0.33867], [0.08239, 0.05628, 0.09339, 0.65847, 0.32917, 0.48483, 0.20733, 1.18679, 0.61785, 0.05667, 0.60659], [0.31113, 0.033, 0.70603, 0.51836, 0.27836, 0.23003, 1.0065, 0.37166, 0.1164, 0.84412, 0.03317], [0.15145, 0.23114, 0.18071, 0.94722, 0.21677, 0.27455, 1.57309, 2.04665, 0.41309, 0.40632, 1.09932]], [[[0.5047, 0.8567, 0.6459, 0.21975, 0.68974, 0.17675, 0.29603, 0.06243, 0.70846, 0.29389, 0.15933], [0.14567, 0.181, 0.42588, 0.39512, 0.44517, 0.20462, 0.70962, 0.55897, 0.97944, 0.25927, 0.84576], [0.81968, 0.27837, 0.01937, 0.37753, 0.89165, 0.15952, 0.20808, 0.34501, 1.91361, 1.16464, 0.58002], [1.18143, 0.6724, 0.09636, 0.32317, 0.105, 1.14574, 0.21428, 0.08011, 0.28584, 0.45691, 0.29294], [0.87503, 0.17439, 0.37996, 0.9479, 0.82968, 0.19014, 0.26178, 0.24144, 0.20872, 0.11756, 0.49468], [1.10142, 1.29654, 0.49522, 0.2389, 0.77306, 0.033, 0.14101, 1.01855, 0.46043, 0.07451, 0.09893], [0.03236, 0.18814, 0.38381, 0.18117, 2.54167, 0.67347, 0.21761, 0.19959, 0.84672, 0.00923, 0.01733], [0.47008, 0.59825, 0.22389, 0.16157, 0.8562, 0.21978, 0.21628, 0.68276, 0.42762, 0.02978, 0.42029], [0.033, 1.16182, 0.60847, 0.23336, 0.11988, 0.79546, 0.45115, 0.03252, 0.71793, 0.12332, 0.13053], [1.45826, 0.58495, 0.31515, 2.38462, 0.29921, 0.16179, 0.18033, 0.78964, 0.15456, 0.4861, 1.18936], [0.59923, 0.47008, 1.0008, 1.58881, 0.40182, 0.39075, 0.16702, 0.60254, 0.08622, 0.16878, 0.22876]], [[0.2892, 0.46111, 0.21212, 0.38212, 0.10871, 0.5579, 1.92945, 0.37554, 0.72862, 0.09729, 0.73834], [1.40517, 0.02509, 0.23984, 0.31543, 0.93929, 0.67678, 0.08893, 0.45614, 0.95242, 0.76528, 0.35395], [0.31486, 0.08705, 0.21929, 0.033, 0.83125, 0.564, 0.40423, 0.84667, 0.12835, 0.66213, 0.75671], [0.06303, 0.56297, 0.52688, 0.35732, 0.13962, 0.08859, 0.20453, 0.44801, 0.13356, 0.62587, 0.55029], [0.16168, 0.14891, 0.03385, 0.09063, 0.86008, 0.26917, 0.29291, 0.83545, 0.57241, 0.08428, 0.46339], [0.44206, 0.31739, 1.91868, 0.82165, 0.60327, 0.57236, 0.00603, 1.04914, 0.47197, 0.4161, 0.29628], [0.55892, 0.16204, 0.62541, 0.46306, 0.1282, 0.27396, 0.14566, 1.98678, 0.28955, 0.50431, 0.03171], [0.55114, 0.16021, 0.53304, 0.03236, 0.79679, 0.23385, 0.25184, 0.02521, 0.12808, 1.38932, 0.425], [0.50219, 0.54925, 0.06291, 1.21501, 0.52149, 0.34282, 0.36427, 0.49915, 1.14313, 0.95223, 0.00881], [0.68816, 0.33378, 0.09635, 0.49166, 0.21207, 0.73672, 0.73994, 0.6766, 0.19543, 0.08177, 0.23608], [1.39137, 0.19785, 0.21153, 0.90118, 2.33042, 1.54299, 1.17757, 0.47302, 0.37977, 0.69963, 0.25108]]], [[0.22537, 0.47103, 0.44475, 0.72635, 1.24153, 0.15564, 0.28772, 0.88179, 0.23223, 0.47626, 0.09992]]]
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
