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
          self.weights = [[[1.03936, 0.57812, 1.24632, 0.08017, 0.10804, 0.11718, 1.22863, 0.08385, 0.67319, 0.83471, 0.47566], [0.27316, 0.15812, 0.37269, 0.53165, 0.15697, 0.03317, 0.36169, 0.34097, 0.15291, 0.23454, 0.21102], [0.78265, 0.28181, 1.26206, 0.11949, 0.5308, 0.98454, 0.23022, 0.29494, 0.09458, 0.39535, 0.08232], [0.74756, 0.14004, 0.33375, 0.88212, 0.75735, 0.28943, 0.07682, 0.97056, 1.16787, 0.11954, 0.99656], [1.02237, 0.1587, 0.50529, 0.30194, 0.03121, 1.40141, 1.64714, 0.385, 1.06856, 0.1019, 1.23469], [0.64017, 0.39945, 0.66795, 0.08552, 2.50072, 0.59083, 0.10877, 0.48619, 0.17343, 1.27575, 0.56869], [0.85643, 0.4601, 0.36957, 0.58496, 0.42095, 0.48446, 0.7016, 0.41736, 0.69851, 0.03334, 0.13924], [1.34964, 0.6555, 0.14356, 0.64235, 0.35157, 0.28545, 0.56879, 0.21319, 0.42374, 0.48684, 0.33872], [0.08198, 0.056, 0.09341, 0.66181, 0.3325, 0.49968, 0.20945, 1.18098, 0.60878, 0.05669, 0.61891], [0.31586, 0.03284, 0.70615, 0.50815, 0.2784, 0.22325, 1.00655, 0.37547, 0.11699, 0.8442, 0.03334], [0.15147, 0.22774, 0.17803, 0.95683, 0.21788, 0.26646, 1.58132, 2.10924, 0.4152, 0.40435, 1.08307]], [[[0.49476, 0.85684, 0.63637, 0.21977, 0.69329, 0.17945, 0.29167, 0.06372, 0.70148, 0.29392, 0.15776], [0.14424, 0.18012, 0.42596, 0.40521, 0.44525, 0.20362, 0.71329, 0.56747, 0.97954, 0.26323, 0.86298], [0.82392, 0.27563, 0.01889, 0.37384, 0.89173, 0.15716, 0.205, 0.34504, 1.95256, 1.18831, 0.59773], [1.18161, 0.67245, 0.09353, 0.33308, 0.1045, 1.16905, 0.20902, 0.07971, 0.28875, 0.47325, 0.2886], [0.87516, 0.17795, 0.38194, 0.94802, 0.83387, 0.194, 0.26053, 0.24883, 0.20669, 0.11582, 0.50731], [1.11263, 1.30316, 0.4953, 0.24134, 0.77311, 0.03252, 0.14034, 1.01868, 0.46512, 0.0764, 0.09993], [0.03268, 0.18816, 0.38579, 0.18299, 2.49171, 0.65694, 0.21764, 0.19863, 0.84263, 0.00933, 0.0176], [0.46777, 0.58069, 0.22845, 0.15998, 0.86058, 0.21118, 0.22178, 0.70017, 0.43417, 0.02993, 0.4141], [0.03368, 1.17365, 0.62079, 0.2299, 0.12109, 0.753, 0.4673, 0.033, 0.72164, 0.12271, 0.12924], [1.47317, 0.58791, 0.32154, 2.39689, 0.29627, 0.16346, 0.17767, 0.78972, 0.15694, 0.50857, 1.19549], [0.5816, 0.46779, 1.03143, 1.51922, 0.4059, 0.38499, 0.16374, 0.60259, 0.08623, 0.16879, 0.22426]], [[0.29506, 0.46578, 0.21536, 0.37648, 0.10658, 0.56642, 1.90099, 0.36815, 0.73602, 0.09587, 0.72385], [1.39831, 0.02535, 0.24595, 0.31864, 0.94884, 0.70804, 0.09119, 0.46776, 0.95731, 0.74647, 0.35937], [0.32129, 0.08619, 0.22043, 0.033, 0.83969, 0.5502, 0.41038, 0.88141, 0.12456, 0.66554, 0.75298], [0.06241, 0.57157, 0.52432, 0.36457, 0.13895, 0.08598, 0.20765, 0.44807, 0.13227, 0.62286, 0.55034], [0.16089, 0.14968, 0.03402, 0.09155, 0.86882, 0.26922, 0.29005, 0.86963, 0.56114, 0.08513, 0.46112], [0.44433, 0.32545, 1.89032, 0.81357, 0.61863, 0.58986, 0.00585, 1.04408, 0.47915, 0.40994, 0.3023], [0.55345, 0.15966, 0.62544, 0.47728, 0.12758, 0.27261, 0.14422, 2.01703, 0.28962, 0.50437, 0.03107], [0.55123, 0.16184, 0.53313, 0.03236, 0.78504, 0.23154, 0.25188, 0.02496, 0.1294, 1.41757, 0.42506], [0.49726, 0.53574, 0.06292, 1.20908, 0.51637, 0.34804, 0.36797, 0.50426, 1.1547, 0.9716, 0.00893], [0.70566, 0.33382, 0.09212, 0.49419, 0.21209, 0.72944, 0.74, 0.68005, 0.18873, 0.08016, 0.23493], [1.44114, 0.19108, 0.21156, 0.89228, 2.31905, 1.4901, 1.20152, 0.48024, 0.37607, 0.70316, 0.25364]]], [[0.22994, 0.46875, 0.44706, 0.73006, 1.24165, 0.1588, 0.27647, 0.88185, 0.23932, 0.47158, 0.09894]]]
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
