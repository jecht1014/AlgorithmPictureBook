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

class Node {
    public:
        vector<long long> edge_value;
        vector<int> next_node;
        long long value = 0;
};

class Graph {
    public:
        int node_num;
        vector<Node> node;
        
        // 辺の重みを1で初期化
        Graph(vector<vector<int>> edge) {
            node_num = edge.size();
            node = vector<Node>(edge.size());
            for (int i = 0; i < edge.size(); i++) {
                node[i].value = i;
                for (int j = 0; j < edge[i].size(); j++) {
                    node[i].push_back(edge[i][j]);
                    node[i].push_back(1);
                }
            }
        }

        // 重み付き辺有
        Graph(vector<vector<int>> edge, vector<vector<long long>> edge_weight) {
            node_num = edge.size();
            node = vector<Node>(edge.size());
            for (int i = 0; i < edge.size(); i++) {
                node[i].value = i;
                for (int j = 0; j < edge[i].size(); j++) {
                    node[i].push_back(edge[i][j]);
                    node[i].push_back(edge_weight[i][j]);
                }
            }
        }

        // ベルマンフォード法(あるノードから全てのノードの最短経路探索)
        vector<long long> bellman_ford(int n) {
            vector<long long> shortest_path(node_num, INF);
            shortest_path[n] = 0;
            for (int _ = 0; _ < node_num-1; _++)
                for (int i = 0; i < node_num; i++)
                    for (int j = 0; j < node[i].next_node.size(); j++)
                        shortest_path[node[i].next_node[j]] = min(shortest_path[node[i].next_node[j]], shortest_path[i]+node[i].edge_value[j]);
            return shortest_path;
        }
};

int main() {
    vector<vector<int>> hen{{1, 2}, {0, 3}, {0}};
    Graph graph(hen);
    vector<long long> shortest_path = graph.bellman_ford(0);
}