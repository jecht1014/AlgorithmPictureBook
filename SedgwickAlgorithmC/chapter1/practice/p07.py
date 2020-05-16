# 加重高速合併アルゴリズム
class Weighted_Quick_Union:
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]
        self.node_num = [1] * N

    def find(self, a):
        if a == self.connected_componet[a]:
            self.reference_count += 1
            return a
        self.reference_count += 1
        return self.find(self.connected_componet[a])
    
    def union(self, a, b):
        self.reference_count = 0
        a_root = self.find(a)
        b_root = self.find(b)
        if (a_root != b_root):
            print(a, b)
            if (self.node_num[a_root] <= self.node_num[b_root]):
                self.connected_componet[a_root] = b_root
                self.node_num[b_root] += self.node_num[a_root]
            else:
                self.connected_componet[b_root] = a_root
                self.node_num[a_root] += self.node_num[b_root]
            print(self.reference_count+1)
            print(self.connected_componet)

weighted_quick_union = Weighted_Quick_Union(7)
weighted_quick_union.union(0, 2)
weighted_quick_union.union(1, 4)
weighted_quick_union.union(2, 5)
weighted_quick_union.union(3, 6)
weighted_quick_union.union(0, 4)
weighted_quick_union.union(6, 0)
weighted_quick_union.union(1, 3)