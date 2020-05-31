/*
http://poj.org/problem?id=3734
行列累乗、漸化式を求め行列累乗で解く問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int MOD = 10007;

vector<vector<ll>> mul(vector<vector<ll>> A, vector<vector<ll>> B) {
    vector<vector<ll>> C(A.size(), vector<ll>(B[0].size(), 0));
    for (int i = 0; i < A.size(); i++)
        for (int j = 0; j < B[0].size(); j++)
            for (int k = 0; k < A[0].size(); k++)
                C[i][j] = (C[i][j] + A[i][k] * B[k][j] % MOD) % MOD;
    return C;
}

vector<vector<ll>> pow(vector<vector<ll>> A, ll n) {
    vector<vector<ll>> B(A.size(), vector<ll>(A[0].size(), 0));
    for (int i = 0; i < B.size(); i++)
        B[i][i] = 1;
    
    while (n > 0) {
        if (n & 1)
            B = mul(B, A);
        A = mul(A, A);
        n = n >> 1;
    }
    return B;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;

        vector<vector<ll>> A = {{2, 1, 0}, {2, 2, 2}, {0, 1, 2}};
        A = pow(A, N);
        cout << A[0][0] << endl;
    }
}