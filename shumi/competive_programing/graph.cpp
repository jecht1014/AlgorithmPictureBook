#include <bits/stdc++.h>
using namespace std;
#define INF 10e12

// graphは隣接表現
vector<vector<long long>> warshall_floyd(vector<vector<long long>> graph) {
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
bool find_negative_loop(vector<edge> es, int start_point, int vertex_num) {
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

int main() {
    vector<vector<int>> hen{{1, 2}, {0, 3}, {0}};
    Graph graph(hen);
    vector<long long> shortest_path = graph.bellman_ford(0);
    print(has_negative_cycle());
}