/*
http://poj.org/problem?id=1064
解を仮定して二分探索を行う問題
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    vector<double> L(N);
    for (int i = 0; i < N; i++)
        cin >> L[i];
    
    double lb = 0, ub = 100000;
    for (int i = 0; i < 100; i++) {
        int num = 0;
        double mid = (ub+lb)/2;
        for (int j = 0; j < N; j++) {
            num += (int)(L[j] / mid);
        }
        if (num >= K)
            lb = mid;
        else
            ub = mid;
    }
    cout << fixed << setprecision(2) << floor(ub * 100) / 100 << endl;
}