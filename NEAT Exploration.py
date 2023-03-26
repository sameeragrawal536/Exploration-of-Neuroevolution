import numpy as np
import random
import matplotlib.pyplot as plt

xdata = []
ind = []
for i in range(100):
    for j in range(7):
        ind.append(random.randint(0, 100))
    xdata.append(ind)
    ind = []

ydata = []
for i in range(100):
    ydata.append(xdata[i][0] * 2.71 + xdata[i][1]*-1.22 + xdata[i][2]*-4.662 + xdata[i][3]*4.7 + xdata[i][4]*-0.4 + xdata[i][5]*9.1 + xdata[i][6]*0.6)
    
xvals = []

yvals = []

class Model:                                                                                                                                                    
    params = np.zeros((1, 1))
    fitness = 0
    
    def __init__(self, xdim, ydim):                                                                                                                         # When creating a new model, the parameters are set completely randomly
        self.params = np.random.rand(xdim, ydim)

    def setParams(self, para):
        self.params = np.copy(para)

    def getParams(self):
        return self.params

    def setFitness(self, fit):
        self.fitness = fit

    def calcFitness(self, xdata, ydata):                                                                                                                    # The fitness, or the measure of how "good" the model is, is in this case calculated by finding the difference between the model's predicted value and the actual value. The lower the fitness is, the better the model, because the closer it is to correctness.
        avg = []
        for i in range(len(xdata)):
            avg.append(abs((np.matmul(xdata[i], self.params)[0]) - ydata[i]))
        fit = sum(avg)/len(avg)
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
                                                                                  
def createPopulation(dims, n):
    population = []
    for i in range(n):                                                                                                                                      # Create population of n models with specified dims (in this case a weights array of 3 rows and 1 column)
        model = Model(dims[0], dims[1])
        population.append(model)
    return population

def fitnessFunction(population, xdata, ydata):                                                                                                              # Evaluate each model's success for evolution algorithm by subtracting the model's output from the expected output, this is not ideal because it makes the fitness function something to be minimized as opposed to maximized, but it's okay.
    for model in population:
        model.calcFitness(xdata, ydata)
    return population
    

def getFittest(population):                                                                                                                                 # Returns the top 10 fittest models because they have the lowest fitness score
    fittest10 = []
    population.sort()
    for i in range(10):
        fittest10.append(population[i])
    return fittest10

def crossOver(fittest10, newPopSize, xdata, ydata, scale):
    newPopulation = []
    
    params = np.zeros(fittest10[0].params.shape)

    for k in range(newPopSize):
        for i in range(len(xdata[0])):
            param = 0
            for j in range(len(fittest10)):
                param += fittest10[j].params[i][0]/10                                                                                                       # Each model in the next generation contains parameters which are the average of the top 10 best models of the previous generation. Simulating the top ten fittest models "mating" and providing the parameters for the new generation.
            param += random.uniform(fittest10[0].getFitness()*-scale, fittest10[0].getFitness()*scale)                                                      # "Mutate" each model by adding random values to its parameters, the mutations are scaled by the fitness value, so the fitter the model, the smaller the mutations are.
            params[i][0] = param
        mod = Model(fittest10[0].getDims()[0], fittest10[0].getDims()[1])
        mod.setParams(params)                                                                                                                                                            
        newPopulation.append(mod)                                                                                                                           # Adding each new model to a new population

    return newPopulation
    

pop = createPopulation([7, 1], 10)
pop = fitnessFunction(pop, xdata, ydata)

for i in range(1000):                                                                                                                                        # Training for 1000 generations
    fittest10 = getFittest(pop)
    pop = crossOver(fittest10, 100, xdata, ydata, 0.03)
    pop = fitnessFunction(pop, xdata, ydata)
    xvals.append(i)
    yvals.append(min(pop).getFitness())

print("Generation: " + str(i))
print(min(pop))
print(max(pop).getFitness(), min(pop).getFitness())

plt.plot(xvals, yvals)

plt.xlabel('Generation')

plt.ylabel('Fitness of Fittest Model (Lower value = more fit)')

plt.title('Fitness Over Generations')

plt.show()                                                                                                                      
