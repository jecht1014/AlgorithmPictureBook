/*
http://poj.org/problem?id=3255
２番目の最短経路を求める問題
*/
#include <bits/stdc++.h>
using namespace std;
#define INF 10e12

struct edge {
    int to;
    long long cost;
};
vector<long long> dijkstra(vector<vector<edge>> es, int start_point) {
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> que;
    vector<long long> shortest_path(es.size(), INF);
    vector<long long> shortest_path2(es.size(), INF);
    shortest_path[start_point] = 0;
    que.push(make_pair(0, start_point));

    while(!que.empty()) {
        pair<long long, int> min_pair = que.top();
        que.pop();
        if (shortest_path2[min_pair.second] < min_pair.first)
            continue;
        for (int i = 0; i < es[min_pair.second].size(); i++) {
            edge e = es[min_pair.second][i];
            long long to_cost = min_pair.first + e.cost;
            if (shortest_path[e.to] > to_cost) {
                swap(shortest_path[e.to], to_cost);
                que.push(make_pair(shortest_path[e.to], e.to));
            }
            if (shortest_path2[e.to] > to_cost && shortest_path[e.to] < to_cost) {
                shortest_path2[e.to] = to_cost;
                que.push(make_pair(shortest_path2[e.to], e.to));
            }
        }
    }
    return shortest_path2;
}

int main() {
    int N, R;
    cin >> N >> R;
    vector<vector<edge>> es(N);
    for (int i = 0; i < R; i++) {
        int a, b, d;
        cin >> a >> b >> d;
        a--; b--;
        edge e1 = {b, d};
        edge e2 = {a, d};
        es[a].push_back(e1);
        es[b].push_back(e2);
    }
    
    vector<long long> shortest_path2 = dijkstra(es, 0);
    cout << shortest_path2[N-1] << endl;
}