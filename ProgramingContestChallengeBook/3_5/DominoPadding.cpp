/*
完全マッチング問題
ビットDP、数え上げ問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e15;

int main(void){
    int n = 3, m = 3;
    vector<string> field = {"...", ".x.", "..."};
    
    vector<vector<vector<int>>> dp(n, vector<vector<int>>(m, vector<int>((1<<m), 0)));
    dp[0][0][0] = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < (1<<m); k++) {
                // 着目しているマスが埋める対象じゃないとき
                if (field[i][j] == 'x') {
                    if (j+1 < m)
                        dp[i][j+1][(k>>1)] += dp[i][j][k];
                    else
                        dp[i+1][0][(k>>1)] += dp[i][j][k];
                }
                else {
                    // 縦の探索
                    if (i+1 < n && field[i+1][j] == '.') {
                        if (j+1 < m)
                            dp[i][j+1][(k>>1) | (1<<(m-1))] += dp[i][j][k];
                        else
                            dp[i+1][0][(k>>1) | (1<<(m-1))] += dp[i][j][k];
                    }
                    // 横の探索
                    if (j+1 < m && field[i][j+1] == '.' && ~((k>>1)&1)) {
                        dp[i][j+1][(k>>1) | 1] += dp[i][j][k];
                    }
                }
            }
        }
    }
    cout << dp[n-1][m-1][1] << endl;
}