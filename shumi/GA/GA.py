import random

class GA:
    def generate_gene(self):
        for i in range(self.gene_num):
            self.gene.append(random.choices(self.genotype, k=self.gene_len))

    def __init__(self, genotype: list, gene_len: int, gene_num: int):
        self.genotype = genotype
        self.gene_len = gene_len
        self.gene_num = gene_num
        self.gene = []
        self.generate_gene()

    def one_point_crossover(self):
        parent = []
        parent = random.sample(self.gene, 2)
        cut_point = random.randint(1, self.gene_len-1)
        children = [parent[0][:cut_point]+parent[1][cut_point:], parent[1][:cut_point]+parent[0][cut_point:]]
        return children

ga = GA([1, 2, 3, 4], 10, 20)
print(ga.one_point_crossover())