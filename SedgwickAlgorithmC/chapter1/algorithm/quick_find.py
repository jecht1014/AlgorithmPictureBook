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
        if (a_root != b_root):
            for i in range(self.N):
                if (self.connected_componet[i] == a_root):
                    self.connected_componet[i] = b_root