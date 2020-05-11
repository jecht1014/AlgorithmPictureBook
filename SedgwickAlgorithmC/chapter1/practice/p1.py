import copy

class UnionFind:
    connected_component = []

    def find(self, p):
        p_idx = -1
        for i in range(len(self.connected_component)):
            for j in range(len(self.connected_component[i])):
                if (self.connected_component[i][j] == p):
                    p_idx = i
            if (p_idx != -1):
                break
        return p_idx
    
    def union(self, a, b):
        a_idx = self.find(a)
        b_idx = self.find(b)
        if (a_idx > b_idx):
            a_idx, b_idx = b_idx, a_idx
            a, b = b, a
        
        if (a_idx == b_idx != -1):
            return
        elif (a_idx == b_idx == -1):
            self.connected_component.append([a, b])
        elif (a_idx == -1 and b_idx != -1):
            self.connected_component[b_idx].append(a)
        else:
            self.connected_component[a_idx].extend(copy.deepcopy(self.connected_component[b_idx]))
            del self.connected_component[b_idx]
        print(a, b)
        print(self.connected_component)

uf = UnionFind()
uf.union(0, 2)
uf.union(1, 4)
uf.union(2, 5)
uf.union(3, 6)
uf.union(0, 4)
uf.union(6, 0)
uf.union(1, 3)