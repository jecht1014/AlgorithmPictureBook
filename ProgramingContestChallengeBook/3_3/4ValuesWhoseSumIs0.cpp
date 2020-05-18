/*
http://poj.org/problem?id=2785
半分全列挙、４つのリストから取り出した数字の和が0になるものがいくつあるか
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int max_n = 4000;
int A[max_n], B[max_n], C[max_n], D[max_n], n;
int AB[max_n*max_n];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    
    // AとBの和を全列挙(O(n^2))
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            AB[i*n+j] = A[i]+B[j];
        }
    }
    sort(AB, AB+n*n);

    // CとDを全列挙して二分探索で数字を探す(O((n^2)*log(n)*2))
    ll res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            res += upper_bound(AB, AB+n*n, -(C[i]+D[j])) - lower_bound(AB, AB+n*n, -(C[i]+D[j]));
        }
    }
    printf("%d\n", res);
}