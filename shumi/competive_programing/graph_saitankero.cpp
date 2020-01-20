// Atcoder abc132 E
// https://atcoder.jp/contests/abc132/tasks/abc132_e
// 有向グラフの最短経路を幅優先探索で探索
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> hen(N);
    
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        hen[u-1].push_back(v-1);
    }
    int S, T;
    cin >> S >> T;
    S--;
    T--;
    
    vector<vector<int>> flag(N, vector<int>(3, 0));
    flag[S][0] = 1;
    queue<vector<ll>> que;
    for (int i = 0; i < hen[S].size(); i++) {
        flag[hen[S][i]][1] = 1;
        vector<ll> a = {hen[S][i], 1, 0};
        que.push(a);
    }
    
    ll ans = -1;
    while(!que.empty()) {
        vector<ll> p = que.front();
        que.pop();
        //cout << p[0] << " " << p[1] << " " << p[2] << endl;
        for (int i = 0; i < hen[p[0]].size(); i++) {
            if (p[1] < 2 && flag[hen[p[0]][i]][p[1]+1] == 0) {
                flag[hen[p[0]][i]][p[1]+1] = 1;
                vector<ll> a = {hen[p[0]][i], p[1]+1, p[2]};
                que.push(a);
            }
            else if (p[1] == 2 && flag[hen[p[0]][i]][0] == 0) {
                if (hen[p[0]][i] == T) {
                    ans = p[2]+1;
                    break;
                }
                flag[hen[p[0]][i]][0] = 1;
                vector<ll> a = {hen[p[0]][i], 0, p[2]+1};
                que.push(a);
            }
        }
        if (ans != -1)
            break;
    }
    cout << ans << endl;
}