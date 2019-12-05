import random
import copy

class GA:
    def generate_gene(self):
        for i in range(self.gene_num):
            self.gene.append(random.choices(self.genotype, k=self.gene_len))

    def __init__(self, genotype: list, gene_len: int, gene_num: int, mutation_rate: float):
        self.genotype = genotype
        self.gene_len = gene_len
        self.gene_num = gene_num
        self.mutation_rate = mutation_rate
        self.gene = []
        self.children_gene = []
        self.fitness = None
        self.generate_gene()

    def one_point_crossover(self):
        parent = random.sample(self.gene, 2)
        cut_point = random.randint(1, self.gene_len-1)
        children = [parent[0][:cut_point]+parent[1][cut_point:], parent[1][:cut_point]+parent[0][cut_point:]]
        self.children_gene += children

    def mutation(self):
        for i in range(len(self.children_gene)):
            for j in range(self.gene_len):
                if (random.random() <= self.mutation_rate):
                    l = copy.deepcopy(self.genotype)
                    l.remove(self.children_gene[i][j])
                    self.children_gene[i][j] = random.choice(l)

    def roulette_method(self):
        self.gene = []
        for i in range(self.gene_num):
            f = copy.deepcopy(self.fitness)
            f_probability = [float(i) / sum(f) for i in f]
            probability_sum = 0
            r = random.random()
            for j in range(len(self.children_gene)):
                probability_sum += f_probability[j]
                if (probability_sum <= r):
                    self.gene.append(copy.deepcopy(self.children_gene[j]))
                    del self.children_gene[j]
                    del self.fitness[j]
                    break
        self.children_gene = []

ga = GA([1, 0], 10, 20, 0.03)
for i in range(20):
    ga.one_point_crossover()
ga.mutation()
ga.fitness = [sum(g) for g in ga.children_gene]
ga.roulette_method()