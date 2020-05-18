/*
オリジナル問題
座標圧縮、配列に収まらないような区切られた区間を数える問題
必要な座標は前後１つだけというところに注目し圧縮
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int max_n = 500;
int W, H, N;
int X1[max_n], X2[max_n], Y1[max_n], Y2[max_n];

int dx[4] = {-1, 0, 0, 1}, dy[4] = {0, -1, 1, 0};

// x1とx2を座標圧縮し圧縮後の幅を返す
int compress(int *x1, int *x2, int w) {
    vector<int> xs; //圧縮しない座標
    
    // x1, x2の座標と前後１つを保存
    for (int i = 0; i < N; i++) {
        for (int d = -1; d <= 1; d++) {
            int tx1 = x1[i]+d, tx2 = x2[i]+d;
            if (1 <= tx1 && tx1 <= W) xs.push_back(tx1);
            if (1 <= tx2 && tx2 <= W) xs.push_back(tx2);
        }
    }

    sort(xs.begin(), xs.end());
    // 重複削除
    xs.erase(unique(xs.begin(), xs.end()), xs.end());

    // 圧縮後のx1,x2の保存
    for (int i = 0; i < N; i++) {
        // xsに存在しない数値分圧縮する
        x1[i] = find(xs.begin(), xs.end(), x1[i]) - xs.begin();
        x2[i] = find(xs.begin(), xs.end(), x2[i]) - xs.begin();
    }
    return xs.size();
}

int main() {
    cin >> W >> H >> N;
    for (int i = 0; i < N; i++)
        cin >> X1[i];
    for (int i = 0; i < N; i++)
        cin >> X2[i];
    for (int i = 0; i < N; i++)
        cin >> Y1[i];
    for (int i = 0; i < N; i++)
        cin >> Y2[i];
    
    // 圧縮
    W = compress(X1, X2, W);
    H = compress(Y1, Y2, H);

    // 二次元空間の塗りつぶし
    bool field[max_n*3][max_n*3];
    for (int i = 0; i < N; i++) {
        for (int y = Y1[i]; y <= Y2[i]; y++) {
            for (int x = X1[i]; x <= X2[i]; x++) {
                field[y][x] = true;
            }
        }
    }

    // 領域の個数を数える
    int res = 0;
    for (int y = 0; y < H; y++) {
        for (int x = 0; x < W; x++) {
            if (field[y][x])
                continue;
            res++;

            // 幅優先探索
            queue<pair<int, int>> que;
            que.push(make_pair(x, y));
            while(!que.empty()) {
                int sx = que.front().first, sy = que.front().second;
                que.pop();

                for (int d = 0; d < 4; d++) {
                    int tx = sx+dx[d], ty = sy+dy[d];
                    if (0 <= tx && tx < W && 0 <= ty && ty < H && !field[ty][tx]) {
                        que.push(make_pair(tx, ty));
                        field[ty][tx] = true;
                    }
                }
            }
        }
    }

    cout << res << endl;
}