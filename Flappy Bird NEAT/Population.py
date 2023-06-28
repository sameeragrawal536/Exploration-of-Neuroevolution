import Bird

class population:
    population = []
    def __init__(self, n):
        self.population = []
        for i in range(n):                                                                                                                                      # Create population of n models with specified dims (in this case a weights array of 3 rows and 1 column)
            bird1 = Bird.bird(100, 100)
            self.population.append(bird1)

    def getFittest(self):                                                                                                                                 # Returns the top 10 fittest models because they have the lowest fitness score
        fittest10 = []
        self.population.sort()
        for i in range(10):
            fittest10.append(self.population[i])
        return fittest10

    def crossOver(fittest10, newPopSize, xdata, ydata, scale):
        newPopulation = []
        
        params = np.zeros(fittest10[0].brain.params.shape)

        for k in range(newPopSize):
            for i in range(len(xdata[0])):
                param = 0
                for j in range(len(fittest10)):
                    param += fittest10[j].brain.params[i][0]/10                                                                                                       # Each model in the next generation contains parameters which are the average of the top 10 best models of the previous generation. Simulating the top ten fittest models "mating" and providing the parameters for the new generation.
                param += random.uniform(fittest10[0].getFitness()*-scale, fittest10[0].getFitness()*scale)                                                      # "Mutate" each model by adding random values to its parameters, the mutations are scaled by the fitness value, so the fitter the model, the smaller the mutations are.
                params[i][0] = param
            bird1 = Bird.bird(100,100)
            bird1.brain.setParams(params)                                                                                                                                                            
            newPopulation.append(bird1)                                                                                                                           # Adding each new model to a new population

        return newPopulation
