/*
オリジナル問題
行列累乗、フィボナッチ数列の第n項を求める問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll M = 10000;
vector<vector<ll>> mul(vector<vector<ll>> A, vector<vector<ll>> B) {
    vector<vector<ll>> C(A.size(), vector<ll>(B[0].size(), 0));
    for (int i = 0; i < A.size(); i++)
        for (int j = 0; j < B[0].size(); j++)
            for (int k = 0; k < A[0].size(); k++)
                C[i][j] += A[i][k] * B[k][j] % M;
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

int main(void){
    ll n;
    cin >> n;

    vector<vector<ll>> A = {{1, 1}, {1, 0}};
    A = pow(A, n);
    cout << A[1][0] << endl;
}