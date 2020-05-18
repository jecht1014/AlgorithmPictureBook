/*
http://poj.org/problem?id=3684
弾性衝突問題、完全弾性衝突のボールの位置を求める問題
ボールが複数ある場合は衝突を無視し座標をソートすることで解く
*/

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const double g = 10.0;
int C, N, H, R, T;
double y[100];

// 時刻Tの時のボールの位置
double calc(int T) {
    if (T < 0)
        return H;
    
    double t = sqrt(2 * H / g);
    int k = (int)(T/t);
    double d;
    if (k % 2 == 0)
        d = T - k*t;
    else
        d = k * t + t - T;
    return H - g * d * d / 2;
}

int main() {
    cin >> C;
    for (int c = 0; c < C; c++) {
        cin >> N >> H >> R >> T;
        for (int i = 0; i < N; i++)
            y[i] = calc(T-i);
        
        sort(y, y+N);
        for (int i = 0; i < N; i++) {
            printf("%.2f%c", y[i] + 2 * R * i / 100.0, i+1 == N ? '\n' : ' ');
        }
    }
}