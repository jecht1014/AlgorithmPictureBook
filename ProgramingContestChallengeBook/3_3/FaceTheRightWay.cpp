/*
http://poj.org/problem?id=3276
反転問題、すべての牛が前を向くのに必要な回転の回数を求める問題
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#include <iostream>
#include <vector>
using namespace std;
typedef long long ll;

int main() {
    int N;
    cin >> N;
    vector<int> fb(N);
    for (int i = 0; i < N; i++) {
        char a;
        cin >> a;
        if (a == 'F')
            fb[i] = 0;
        else
            fb[i] = 1;
    }

    int M = N;
    int K = 1;
    for (int k = 1; k <= N; k++) {
        vector<int> f(N-(k-1), 0);
        int sum = 0;
        int m = 0;
        for (int i = 0; i+k <= N; i++) {
            if ((fb[i]+sum) % 2 == 1) {
                m++;
                f[i] = 1;
                sum++;
            }

            if (i-k+1 >= 0)
                sum -= f[i-k+1];
        }

        if (M > m) {
            bool is_not_break = true;
            for (int i = N-k+1; i < N; i++) {
                if ((fb[i]+sum)%2 == 1) {
                    is_not_break = false;
                    break;
                }
                if (i-k+1 >= 0)
                    sum -= f[i-k+1];
            }
            if (is_not_break) {
                M = m;
                K = k;
            }
        }
    }
    cout << K << " " << M << endl;
}