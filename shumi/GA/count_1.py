import GA

ga = GA.GA([1, 0], 10, 20, 0.03)
while (True):
    for i in range(20):
        ga.one_point_crossover()
    ga.mutation()
    ga.fitness = [sum(g) for g in ga.children_gene]
    print(max(ga.fitness))
    if (max(ga.fitness) == 10):
        break
    
    ga.gene = []
    ga.roulette_method(20)