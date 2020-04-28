/*
http://poj.org/problem?id=3061
和がS以下の最小部分列を求める
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n, S;
    cin >> n >> S;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    
    int ans = n+1;
    int s = 0, t = 0, sum = 0;
    for(;;) {
        while(sum < S && t < n) {
            sum += a[t];
            t++;
        }

        if (sum < S)
            break;
        
        ans = min(ans, t-s);
        sum -= a[s];
        s++;
    }

    if (ans > n)
        ans = 0;
    cout << ans << endl;
}