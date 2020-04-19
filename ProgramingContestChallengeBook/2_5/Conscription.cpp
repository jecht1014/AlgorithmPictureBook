#include <bits/stdc++.h>
using namespace std;
#define INF 10e12

struct edge {
    int u, v;
    long long cost;
};

bool comp(const edge& e1, const edge& e2) {
    return e1.cost < e2.cost;
}

struct UnionFind {
    vector<int> par; // par[i]:iの親の番号 根のときはpar[i]=i

    //最初は全てが根であるとして初期化
    UnionFind(int N) : par(N) {
        for(int i = 0; i < N; i++) par[i] = i;
    }

    // データxが属する木の根を再帰で得る：root(x) = {xの木の根}
    int root(int x) {
        if (par[x] == x) return x;
        return par[x] = root(par[x]);
    }

    // xとyの木を併合
    void unite(int x, int y) {
        int rx = root(x);
        int ry = root(y);
        if (rx == ry) return;
        par[rx] = ry;
    }
    
     // 2つのデータx, yが属する木が同じならtrueを返す
    bool same(int x, int y) {
        return root(x) == root(y);
    }
};

vector<edge> kruskal(vector<edge> es, int vertex_num) {
    sort(es.begin(), es.end(), comp);
    UnionFind uftree(vertex_num);
    vector<edge> ans_graph;
    for (int i = 0; i < es.size(); i++) {
        if (!uftree.same(es[i].u, es[i].v)) {
            uftree.unite(es[i].u, es[i].v);
            ans_graph.push_back(es[i]);
        }
    }
    return ans_graph;
}

int main() {
    int N, M, R;
    cin >> N >> M >> R;
    vector<edge> es(R);
    for (int i = 0; i < R; i++) {
        cin >> es[i].u >> es[i].v >> es[i].cost;
        es[i].v = es[i].v + N; es[i].cost = -es[i].cost;
    }
    
    vector<edge> tree = kruskal(es, N+M);
    int ans = (N+M)*10000;
    for (int i = 0; i < tree.size(); i++)
        ans += tree[i].cost;
    cout << ans << endl;
}