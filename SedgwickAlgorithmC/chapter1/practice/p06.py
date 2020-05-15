# 加重高速合併アルゴリズム
class Weighted_Quick_Union:
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]
        self.node_num = [1] * N

    def find(self, a):
        if a == self.connected_componet[a]:
            return a
        return self.find(self.connected_componet[a])
    
    def union(self, a, b):
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
            print(self.connected_componet)

print('適当に数字を選んだ場合(図1.7)')
weighted_quick_union = Weighted_Quick_Union(10)
weighted_quick_union.union(4, 3)
weighted_quick_union.union(4, 9)
weighted_quick_union.union(0, 8)
weighted_quick_union.union(2, 3)
weighted_quick_union.union(6, 5)
weighted_quick_union.union(5, 9)
weighted_quick_union.union(3, 7)
weighted_quick_union.union(8, 4)
weighted_quick_union.union(1, 6)

print('\n計算量が最悪になるように数字を選んだ場合(図1.8)')
weighted_quick_union = Weighted_Quick_Union(10)
weighted_quick_union.union(1, 0)
weighted_quick_union.union(3, 2)
weighted_quick_union.union(5, 4)
weighted_quick_union.union(7, 6)
weighted_quick_union.union(9, 8)
weighted_quick_union.union(2, 0)
weighted_quick_union.union(6, 4)
weighted_quick_union.union(4, 0)
weighted_quick_union.union(6, 8)