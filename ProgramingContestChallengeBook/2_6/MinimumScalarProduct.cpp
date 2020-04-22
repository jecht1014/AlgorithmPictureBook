/*
スカラーの内積を最小化する問題
https://code.google.com/codejam/contest/32016/dashboard#s=p0
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int T;
    cin >> T;
    for (int j = 1; j <= T; j++) {
        int n;
        cin >> n;
        vector<ll> v1(n), v2(n);
        for (int i = 0; i < n; i++)
            cin >> v1[i];
        for (int i = 0; i < n; i++)
            cin >> v2[i];
        
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end(), greater<ll>());

        ll ans = 0;
        for (int i = 0; i < n; i++)
            ans += v1[i]*v2[i];
        cout << "Case #" << j << ": " << ans << endl;
    }
}