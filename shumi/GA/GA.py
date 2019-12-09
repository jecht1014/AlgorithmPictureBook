import random
import copy

class GA:
    def generate_gene(self):
        for i in range(self.gene_num):
            if (self.lethal_gene_avoidance):
                self.gene.append(random.sample(self.genotype, len(self.genotype)))
            else:
                self.gene.append(random.choices(self.genotype, k=self.gene_len))

    def __init__(self, genotype: list, gene_len: int, gene_num: int, mutation_rate: float, lethal_gene_avoidance=False):
        self.genotype = genotype
        self.gene_len = gene_len
        self.gene_num = gene_num
        self.mutation_rate = mutation_rate
        self.lethal_gene_avoidance = lethal_gene_avoidance
        self.gene = []
        self.children_gene = []
        self.fitness = None
        self.generate_gene()

    def base_sequence_table_encode(self, gene1, gene2):
        c1 = [1] * len(gene1)
        c2 = []
        gene1_c = copy.deepcopy(gene1)
        for s in gene2:
            c2.append(gene1_c.index(s)+1)
            del gene1_c[gene1_c.index(s)]

        return c1, c2

    def base_sequence_table_decode(self, base_sequence_table, c1, c2):
        p1 = []
        p2 = []
        base_sequence_table_c = copy.deepcopy(base_sequence_table)
        for s in c1:
            p1.append(base_sequence_table_c[s-1])
            del base_sequence_table_c[s-1]
        base_sequence_table_c = copy.deepcopy(base_sequence_table)
        for s in c2:
            p2.append(base_sequence_table_c[s-1])
            del base_sequence_table_c[s-1]
        return p1, p2
        
    def one_point_crossover(self):
        parent = random.sample(self.gene, 2)
        if self.lethal_gene_avoidance:
            base_sequence_table = copy.deepcopy(parent[0])
            parent[0], parent[1] = self.base_sequence_table_encode(parent[0], parent[1])
        cut_point = random.randint(1, self.gene_len-1)
        children = [parent[0][:cut_point]+parent[1][cut_point:], parent[1][:cut_point]+parent[0][cut_point:]]
        if self.lethal_gene_avoidance:
            children[0], children[1] = self.base_sequence_table_decode(base_sequence_table, children[0], children[1])

        self.children_gene += children

    def mutation(self):
        for i in range(len(self.children_gene)):
            if self.lethal_gene_avoidance:
                if (random.random() <= self.mutation_rate):
                    a = random.sample(list(range(self.gene_len)), 2)
                    tmp = self.children_gene[i][a[0]]
                    self.children_gene[i][a[0]] = self.children_gene[i][a[1]]
                    self.children_gene[i][a[1]] = tmp
            else:
                for j in range(self.gene_len):
                    if (random.random() <= self.mutation_rate):
                        l = copy.deepcopy(self.genotype)
                        l.remove(self.children_gene[i][j])
                        self.children_gene[i][j] = random.choice(l)

    def roulette_method(self, num, high_or_low='high'):
        # 低いほど良い場合の処理
        if high_or_low == 'low':
            self.fitness = [abs(f-(max(self.fitness)+1)) for f in self.fitness]
        for i in range(num):
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

#ga = GA([0, 1, 2, 3], 4, 4, 0.03, True)
#for i in range(20):
#    ga.one_point_crossover()
#print(ga.gene)
#print(ga.children_gene)
#ga.mutation()
#ga.fitness = [sum(g) for g in ga.children_gene]
#ga.roulette_method()