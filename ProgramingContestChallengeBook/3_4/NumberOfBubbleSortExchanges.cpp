/*
オリジナル問題
Binary Indexed Tree、バブルソートの交換回数を数える問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct BIT {
    int N;
    vector<int> values;

    // [1,n]
    BIT(int n) : values(n+1, 0) {
        N = n;
    }

    int sum(int i) {
        int s = 0;
        while (i > 0) {
            s += values[i];
            i -= i & -i; // 一番下の位の1を0に変える
        }
        return s;
    }

    void add(int i, int x) {
        while (i <= N) {
            values[i] += x;
            i += i & -i;
        }
    }
};

int main() {
    int n;
    cin >> n;
    BIT bit(n);

    ll ans = 0;
    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        ans += i - bit.sum(a);
        bit.add(a, 1);
    }

    cout << ans << endl;
}