#include <bits/stdc++.h>
using namespace std;
#define INF 10e12

// graphは隣接リスト
vector<vector<long long>> warshall_floyd(vector<vector<long long>> graph) {
    for (int i = 0; i < graph.size(); i++)
        graph[i][i] = 0;
    for (int k = 0; k < graph.size(); k++){
        for (int i = 0; i < graph.size(); i++) {
            for (int j = 0; j < graph.size(); j++) {
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
            }
        }
    }
    return graph;
}

//ベルマンフォード法(負の閉路がある場合は使えない) O(V*E)
//最短経路探索
struct edge {
    int from;
    int to;
    long long cost;
};
vector<long long> bellman_ford(vector<edge> es, int start_point, int vertex_num) {
    vector<long long> shortest_path(vertex_num, INF);
    shortest_path[start_point] = 0;
    for (int i = 0; i < vertex_num-1; i++) {
        for (int j = 0; j < es.size(); j++) {
            shortest_path[es[j].to] = min(shortest_path[es[j].to], shortest_path[es[j].from]+es[j].cost);
        }
    }
    return shortest_path;
}

// 負の閉路の探索 O(V*E)
bool has_negative_loop(vector<edge> es, int start_point, int vertex_num) {
    vector<long long> shortest_path(vertex_num, INF);
    shortest_path[start_point] = 0;
    for (int i = 0; i < vertex_num; i++) {
        for (int j = 0; j < es.size(); j++) {
            if (shortest_path[es[j].to] > shortest_path[es[j].from]+es[j].cost) {
                shortest_path[es[j].to] = shortest_path[es[j].from]+es[j].cost;
                if (i == vertex_num-1)
                    return true;
            }
        }
    }
    return false;
}

// ダイクストラ法(隣接リスト　負の重みなし) O(E log V)
// 最短経路探索
// pair<long long, int> は(cost, vertex)の組み合わせ
struct edge {
    int to;
    long long cost;
};
vector<long long> dijkstra(vector<vector<edge>> es, int start_point) {
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> que;
    vector<long long> shortest_path(es.size(), INF);
    shortest_path[start_point] = 0;
    que.push(make_pair(0, start_point));

    while(!que.empty()) {
        pair<long long, int> min_pair = que.top();
        que.pop();
        if (shortest_path[min_pair.second] < min_pair.first)
            continue;
        for (int i = 0; i < es[min_pair.second].size(); i++) {
            edge e = es[min_pair.second][i];
            if (shortest_path[e.to] > shortest_path[min_pair.second]+e.cost) {
                shortest_path[e.to] = shortest_path[min_pair.second]+e.cost;
                que.push(make_pair(shortest_path[e.to], e.to));
            }
        }
    }
    return shortest_path;
}

// 有効グラフのパスを逆にしたグラフを返す関数
vector<vector<edge>> get_reverse_graph(vector<vector<edge>> graph) {
    vector<vector<edge>> reverse_graph(graph.size());
    for (int i = 0; i < graph.size(); i++) {
        for (int j = 0; j < graph[i].size(); j++) {
            edge e = {i, graph[i][j].cost};
            reverse_graph[graph[i][j].to].push_back(e);
        }
    }
    return reverse_graph;
}

// グラフ隣接リストの最短経路復元
vector<int> restore_shortest_path(vector<vector<edge>> graph, vector<long long> shortest_path, int start_point, int end_point) {
    vector<vector<edge>> reverse_graph = get_reverse_graph(graph);
    queue<vector<int>> current_restored_path_que;
    que.push(vector<int>(1, end_point));
    while(true) {
        vector<int> restored_path = current_restored_path_que.front();
        int current_vertex  = restored_path[restored_path.size()-1];
        current_restored_path_que.pop();
        for (int i = 0; i < reverse_graph[current_vertex].size(); i++) {
            edge e = reverse_graph[current_vertex][i];
            if (shortest_path[current_vertex]-e.cost == shortest_path[e.to]) {
                restored_path.push_back(e.to);
                current_restored_path_que.push(restored_path);
                if (e.to == start_point) {
                    vector<int> result = current_restored_path_que.back();
                    reverse(result.begin(), result.end());
                    return result;
                }
            }
        }
    }
}

// prim法による最小全域木
vector<vector<edge>> prim(vector<vector<edge>> graph) {
    vector<vector<edge>> minimum_spanning_tree(graph.size());
    vector<bool> used(graph.size(), false);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minimum_edge_que;
    minimum_edge_que.push(make_pair(0, 0));
    int count_used = 0;
    int before_vertex = -1;

    while(true) {
        pair<long long, int> add_vertex;
        while(!minimum_edge_que.empty()) {
            add_vertex = minimum_edge_que.top();
            minimum_edge_que.pop();
            if (!used[add_vertex.second]) {
                used[add_vertex.second] = true;
                count_used++;
                if (before_vertex != -1) {
                    edge e = {add_vertex.second, add_vertex.first};
                    minimum_spanning_tree[before_vertex].push_back(e);
                    e.to = before_vertex;
                    minimum_spanning_tree[add_vertex.second].push_back(e);
                }
                before_vertex = add_vertex.second;
                break;
            }
        }

        if (count_used == graph.size())
            break;

        for (int i = 0; i < graph[add_vertex.second].size(); i++) {
            edge e = graph[add_vertex.second][i];
            if (!used[e.to])
                minimum_edge_que.push(make_pair(e.cost, e.to));
        }
    }
    return minimum_spanning_tree;
}

// クラスカル法による最小全域木の構築
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
    sort(es.begin(), es+es.end(), comp);
    UnionFind uftree(vertex_num);
    vector<edge> ans_graph;
    for (int i = 0; i < es.size(); i++) {
        if (!uftree.same(es[i].u, es[i].v)) {
            uftree.unit(es[i].u, es[i].v);
            ans_graph.push_back(es[i]);
        }
    }
    return ans_graph;
}

int main() {
    vector<vector<int>> hen{{1, 2}, {0, 3}, {0}};
    Graph graph(hen);
    vector<long long> shortest_path = graph.bellman_ford(0);
    print(has_negative_cycle());
}