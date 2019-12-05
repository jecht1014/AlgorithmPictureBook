import GA
import numpy as np
import math

i = np.arange(0, 1, 0.1)
x = list(np.cos(2*np.pi*i))
y = list(np.sin(2*np.pi*i))

def distance(i, j):
    return math.sqrt(math.pow(x[i]-x[j], 2) + pow(y[i]-y[j], 2))
def all_distance(l):
    return sum([distance(l[i], l[i+1]) for i in range(len(l)-1)])

ga = GA.GA(list(range(10)), 10, 10, 0.03, True)
for j in range(200):
    for i in range(10):
        ga.one_point_crossover()
    
    ga.mutation()
    ga.fitness = [all_distance(g) for g in ga.children_gene]
    print(max(ga.fitness))
    ga.roulette_method()