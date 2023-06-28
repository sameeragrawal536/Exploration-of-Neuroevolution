import numpy as np

class Model:                                                                                                                                                    
    params = np.zeros((1, 1))
    fitness = 0
    
    def __init__(self, xdim, ydim):                                                                                                                         # When creating a new model, the parameters are set completely randomly
        self.params = np.random.randn(xdim, ydim)
        self.fitness = 0

    def setParams(self, para):
        self.params = np.copy(para)

    def forwardProp(self, data):
        #x = np.asmatrix(data)
        y = (np.matmul(data, self.params))[0]
        y = 1/(1 + np.exp(-y))
        print(y)
        return (y>0.5)

    def getParams(self):
        return self.params

    def setFitness(self, fit):
        self.fitness = fit

    def getFitness(self):
        return self.fitness

    def getDims(self):
        return self.params.shape

    def __lt__ (self, other):
        return self.getFitness() < other.getFitness()

    def __gt__ (self, other):
        return self.getFitness() > other.getFitness()

    def __str__(self):
        output = ""
        for i in self.params:
            output += str(i[0])
            output += " "
        return output
