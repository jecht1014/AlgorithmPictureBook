/*
http://poj.org/problem?id=2686
bitDP、特殊な最短経路探索問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int INF = 10000000;
int main() {
    while (true) {
        int n, m, p, a, b;
        cin >> n >> m >> p >> a >> b;
        if (n == 0 && m == 0 && p == 0 && a == 0 && b == 0)
            break;
        
        a--; b--;
        vector<int> t(n);
        for (int i = 0; i < n; i++)
            cin >> t[i];
        
        vector<vector<int>> d(m, vector<int>(m, INF));
        for (int i = 0; i < p; i++) {
            int x, y, z;
            cin >> x >> y >> z;
            d[x-1][y-1] = z;
            d[y-1][x-1] = z;
        }

        vector<vector<double>> dp((1<<n), vector<double>(m, INF));
        dp[0][a] = 0;
        for (int i = a; i < m; ) {
            for (int j = 0; j < (1<<n); j++) {
                if (dp[j][i] != INF) {
                    for (int k = 0; k < m; k++) {
                        if (d[i][k] != INF) {
                            for (int h = 0; h < n; h++) {
                                if (!(j>>h & 1)) {
                                    dp[j|(1<<h)][k] = min(dp[j|(1<<h)][k], dp[j][i] + d[i][k]/(double)t[h]);
                                    //cout << i << " " << k << " " << dp[j][i] << " " << dp[j|(1<<h)][k] << endl;
                                }
                            }
                        }
                    }
                }
            }

            if (i == 0)
                i = a+1;
            else if (i <= a)
                i--;
            else
                i++;
        }
        double ans = INF;
        for (int i = 0; i < (1<<n); i++)
            ans = min(ans, dp[i][b]);
        if (ans != INF)
            printf("%.3f\n", ans);
        else
            printf("Impossible\n");
    }
}