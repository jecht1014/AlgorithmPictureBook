#include <bits/stdc++.h>
using namespace std;

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

int main() {
    vector<vector<int>> hen{{1, 2}, {0, 3}, {0}};
    vector<set<int>> path = ne_path(hen, 0);
    for (int i = 0; i < path.size(); i++) {
        for (auto x : path[i]) {
            cout << x << " ";
        }
        cout << endl;
    }
}