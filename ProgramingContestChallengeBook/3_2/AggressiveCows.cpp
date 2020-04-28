/*
http://poj.org/problem?id=1064
解を仮定して二分探索を行う問題　最小値の最大化
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int N, M;
    cin >> N >> M;
    vector<ll> x(N);
    for (int i = 0; i < N; i++)
        cin >> x[i];
    sort(x.begin(), x.end());

    ll lb = 0, ub = 1e10;
    while(ub-lb > 1) {
        ll mid = (lb+ub)/2;
        int cow_num = 1;
        ll before_x = x[0];
        for (int i = 1; i < N; i++) {
            if (x[i]-before_x >= mid) {
                cow_num++;
                before_x = x[i];
            }
        }

        if (cow_num >= M)
            lb = mid;
        else
            ub = mid;
    }
    cout << lb << endl;
}