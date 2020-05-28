
/*
巡回セールスマン問題
ビットDP
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e15;

int main() {
    int n = 5;
    vector<vector<ll>> dp(1 << n, vector<ll>(n, INF));
    vector<vector<ll>> d(n, vector<ll>(n, INF));
    d[0][1] = 3; d[0][3] = 4;
    d[1][2] = 5;
    d[2][0] = 4; d[2][3] = 5;
    d[3][4] = 3;
    d[4][0] = 7; d[4][1] = 6;
    
    // それぞれのノードを最後に訪れる時の最短経路を探索
    dp[1][0] = 0;
    for (int i = 1; i < (1 << n); i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                if (dp[i|(1<<j)][j] > dp[i][k] + d[k][j]) {
                    dp[i|(1<<j)][j] = dp[i][k] + d[k][j];
                    //cout << i << " " << j << " " << dp[i | (1 << j)] << endl;
                }
            }
        }
    }
    
    // 最初のノードに戻ってくる時の計算
    ll ans = INF;
    for (int i = 0; i < n; i++)
        ans = min(ans, dp[(1 << n)-1][i] + d[i][0]);
    cout << ans << endl;
}