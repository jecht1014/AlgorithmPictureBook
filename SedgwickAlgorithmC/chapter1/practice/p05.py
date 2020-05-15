# 高速合併アルゴリズム
class Quick_Union:
    reference_count = 0
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]

    def find(self, a):
        self.reference_count += 1
        if a == self.connected_componet[a]:
            return a
        return self.find(self.connected_componet[a])
    
    def union(self, a, b):
        self.reference_count = 0
        a_root = self.find(a)
        b_root = self.find(b)
        if (a_root != b_root):
            print(a, b)
            self.connected_componet[a_root] = b_root
            self.reference_count += 1
            print(self.connected_componet)
        print('reference count: %d' % self.reference_count)

quick_union = Quick_Union(7)
quick_union.union(0, 2)
quick_union.union(1, 4)
quick_union.union(2, 5)
quick_union.union(3, 6)
quick_union.union(0, 4)
quick_union.union(6, 0)
quick_union.union(1, 3)