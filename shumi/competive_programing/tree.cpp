#include <bits/stdc++.h>
using namespace std;

class Node {
    public:
        vector<int> children;
        vector<int> edge_value;
        int value;
        int parent;
};

class Tree {
    public:
        int root;
        int node_num;
        vector<Node> node;
        
        Tree(vector<vector<int>> hen, int r) {
            root = r;
            node_num = hen.size();
            node = vector<Node>(hen.size());
            
            queue<int> v;
            v.push(root);
            node[root].parent = -1;
            int edge_num = 0;
            while(!v.empty()) {
                int tyoten = v.front();
                node[tyoten].value = tyoten;
                v.pop();
                for (int i = 0; i < hen[tyoten].size(); i++) {
                    int child = hen[tyoten][i];
                    if (child != node[tyoten].parent) {
                        node[tyoten].children.push_back(child);
                        node[tyoten].edge_value.push_back(edge_num);
                        edge_num++;
                        node[child].parent = tyoten;
                        v.push(child);
                    }
                }
            }
        }
};

// 2つの頂点を入力として与えることで、最近共通祖先(lca)を求める
int lca(Tree tree, pair<int, int> uv) {
    if (uv.first == tree.root || uv.second == tree.root)
        return tree.root;
    else {
        set<int> parent_set{uv.first};
        int parent = uv.first;
        while(parent != tree.root) {
            parent = tree.node[parent].parent;
            parent_set.insert(parent);
        }

        parent = uv.second;
        while(parent != tree.root) {
            if (parent_set.count(parent))
                return parent;
            parent = tree.node[parent].parent;
        }
    }
}

// ルートから頂点までの辺の累積和(論理和)
vector<set<pair<int, int>>> tree_edge_partial_set(Tree tree) {
    vector<set<pair<int, int>>> partial_set(tree.node_num);
    queue<Node> value;
    value.push(tree.node[tree.root]);
    queue<set<pair<int, int>>> value_set;
    value_set.push(set<pair<int, int>>({}));
    while(!value.empty()) {
        Node v = value.front();
        set<pair<int, int>> v_set = value_set.front();
        value.pop();
        value_set.pop();
        partial_set[v.value] = v_set;
        for (int i = 0; i < v.children.size(); i++) {
            value.push(tree.node[v.children[i]]);
            set<pair<int, int>> v_set_c(v_set);
            v_set_c.insert(make_pair(v.value, v.children[i]));
            value_set.push(v_set_c);
        }
    }
    
    return partial_set;
}

// 上のbitsetバージョン
vector<bitset<59>> tree_edge_partial_set(Tree tree) {
    vector<bitset<59>> partial_set(tree.node_num);
    queue<Node> value;
    value.push(tree.node[tree.root]);
    queue<bitset<59>> value_set;
    value_set.push(bitset<59>(0));
    while(!value.empty()) {
        Node v = value.front();
        bitset<59> v_set = value_set.front();
        value.pop();
        value_set.pop();
        partial_set[v.value] = v_set;
        for (int i = 0; i < v.children.size(); i++) {
            value.push(tree.node[v.children[i]]);
            bitset<59> v_set_c(v_set);
            v_set_c[v.edge_value[i]] = 1;
            value_set.push(v_set_c);
        }
    }
    
    return partial_set;
}

// ルートから頂点までに通る頂点の累積和(論理和)
vector<set<int>> tree_vertex_partial_set(Tree tree) {
    vector<set<int>> partial_set(tree.node_num);
    queue<Node> value;
    value.push(tree.node[tree.root]);
    queue<set<int>> value_set;
    value_set.push(set<int>({tree.root}));
    while(!value.empty()) {
        Node v = value.front();
        set<int> v_set = value_set.front();
        value.pop();
        value_set.pop();
        
        partial_set[v.value] = v_set;
        for (int i = 0; i < v.children.size(); i++) {
            value.push(tree.node[v.children[i]]);
            set<int> v_set_c(v_set);
            v_set_c.insert(v.children[i]);
            value_set.push(v_set_c);
        }
    }
    
    return partial_set;
}

// 入力のnodeと全てのnodeの距離を幅優先探索で計算する関数
vector<int> tree_dist_bfs(Tree tree, Node node) {
    vector<int> dist(tree.node_num, -1);
    queue<pair<int, Node>> que;
    que.push(make_pair(0, node));
    while(!que.empty()) {
        pair<int, Node> p = que.front();
        que.pop();
        dist[p.second.value] = p.first;
        
        // 親ノードの探索
        // 親がいなくて未探索の場合
        if (p.second.parent != -1)
            if (dist[p.second.parent] == -1)
                que.push(make_pair(p.first+1, tree.node[p.second.parent]));
        
        // 子ノードの探索
        for (int i = 0; i < p.second.children.size(); i++)
            if (dist[p.second.children[i]] == -1)
                que.push(make_pair(p.first+1, tree.node[p.second.children[i]]));
    }
    
    return dist;
}

int main() {
    //int n = 3;
    vector<vector<int>> hen{{1}, {0, 2}, {1}};
    
    Tree tree(hen, 0);
    for (int i = 0; i < tree.node.size(); i++) {
        cout << tree.node[i].parent << endl;
    }

    vector<int> v_dist = tree_dist_bfs(tree, tree.node[0]);
}