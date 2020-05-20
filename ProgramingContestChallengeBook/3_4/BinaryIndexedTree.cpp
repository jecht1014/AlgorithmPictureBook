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
    BIT bit(10);
    for (int i = 1; i <= 10; i++)
        bit.add(i, i);
    for (int i = 1; i <= 10; i++)
        cout << bit.sum(i) << endl;
}