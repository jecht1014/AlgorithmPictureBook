# 高速併合アルゴリズム
class Quick_Union:
    def __init__(self, N):
        self.N = N
        self.connected_componet = [i for i in range(N)]

    def find(self, a):
        if a == self.connected_componet[a]:
            return a
        return self.find(self.connected_componet[a])
    
    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if (a_root != b_root):
            self.connected_componet[a_root] = b_root