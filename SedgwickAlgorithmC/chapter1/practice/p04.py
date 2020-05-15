# 高速発見アルゴリズム
class Quick_Find:
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]

    def find(self, a):
        return self.connected_componet[a]
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        reference_count = 2
        if (a_root != b_root):
            print(a, b)
            for i in range(self.N):
                reference_count += 1
                if (self.connected_componet[i] == a_root):
                    self.connected_componet[i] = b_root
            print(self.connected_componet)
        print('reference count: %d' % reference_count)

quick_find = Quick_Find(7)
quick_find.union(0, 2)
quick_find.union(1, 4)
quick_find.union(2, 5)
quick_find.union(3, 6)
quick_find.union(0, 4)
quick_find.union(6, 0)
quick_find.union(1, 3)