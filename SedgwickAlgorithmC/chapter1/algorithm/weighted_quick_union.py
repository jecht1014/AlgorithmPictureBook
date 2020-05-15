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
        self.reference_count = 0
        a_root = self.find(a)
        b_root = self.find(b)
        if (a_root != b_root):
            # ノード数が多い方にノード数が小さい方をつなげる処理
            if (self.node_num[a_root] <= self.node_num[b_root]):
                self.connected_componet[a_root] = b_root
                self.node_num[b_root] += self.node_num[a_root]
            else:
                self.connected_componet[b_root] = a_root
                self.node_num[a_root] += self.node_num[b_root]