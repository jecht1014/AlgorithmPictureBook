/*
http://poj.org/problem?id=3279
二次元の回転を行う問題
一行目のひっくり返し方を全探索することで対応
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int dx[5] = {-1, 0, 0, 0, 1};
const int dy[5] = {0, -1, 0, 1, 0};
int N, M;
int tile[15][15];
int flip[15][15];
int opt[15][15]; //最適解保存用

int get(int x, int y) {
    int c = tile[x][y];
    for (int d = 0; d < 5; d++) {
        int x2 = x+dx[d];
        int y2 = y+dy[d];
        if (0 <= x2 && x2 < M && 0 <= y2 && y2 < N)
            c += flip[x2][y2];
    }
    return c%2;
}

int sum_change_tile() {
    int num = 0;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            num += flip[i][j];
    return num;
}

int calc() {
    for (int i = 1; i < M; i++) {
        for (int j = 0; j < N; j++) {
            // 1個上が黒ならば
            if (get(i-1, j) == 1) {
                flip[i][j] = 1;
            }
        }
    }

    for (int j = 0; j < N; j++) {
        if (get(M-1, j) == 1)
            return -1;
    }

    // 反転回数を数え上げる
    return sum_change_tile();
}

int main() {
    cin >> M >> N;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < N; j++)
            cin >> tile[i][j];

    int res = 15*15+1;    
    for (int i = 0; i < 1 << N; i++) {
        for (int m = 0; m < M; m++)
            for (int n = 0; n < N; n++)
                flip[m][n] = 0;
        for (int j = 0; j < N; j++) {
            flip[0][N-1-j] = i >> j & 1;
        }

        int num = calc();
        if (0 <= num && num < res) {
            res = num;
            memcpy(opt, flip, sizeof(flip));
        }
    }

    if (res == 15*15+1)
        cout << "IMPOSSIBLE" << endl;
    else {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                cout << opt[i][j];
                if (j != N-1)
                    cout << " ";
                else
                    cout << endl;
            }
        }
    }
}