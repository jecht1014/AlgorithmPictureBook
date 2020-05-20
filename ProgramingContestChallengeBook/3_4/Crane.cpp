/*
http://poj.org/problem?id=2991
セグメント木、N個の接続されたクレーンの先端の座標を求める問題
*/
#define _USE_MATH_DEFINES
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct SegmentTree {
    int leaf_node_num;
    vector<double> x, y, ang;
    
    SegmentTree(int input_num) {
        leaf_node_num = 1;
        while (leaf_node_num < input_num)
            leaf_node_num *= 2;
        
        for (int i = 0; i < 2*leaf_node_num-1; i++) {
            x.push_back(0);
            y.push_back(0);
            ang.push_back(0);
        }
    }

    // k番目の値をaに変更
    void update(int k,  double a) {
        k += leaf_node_num-1;
        
        y[k] = a;
        // rootに向かって遡って更新
        while (k > 0) {
            k = (k-1) / 2;
            y[k] = y[k*2+1] + y[k*2+2];
        }
    }

    void change(int s, double a, int k=0, int l=0, int r=-1) {
        // 最初のクエリのとき
        if (r == -1)
            r = leaf_node_num;

        if (s <= l)
            return;
        else if (s < r) {
            int chl = k*2 + 1, chr = k*2 + 2;
            int m = (l+r) / 2;
            change(s, a, chl, l, m);
            change(s, a, chr, m, r);

            // 変更したノードより右にあるノードの角度を変更
            if (s <= m)
                ang[k] += a;
            double s = sin(ang[k]), c = cos(ang[k]);
            // ベクトルの回転(加法定理)
            x[k] = x[chl] + (c * x[chr] - s * y[chr]);
            y[k] = y[chl] + (s * x[chr] + c * y[chr]);
        }
    }
};

int main() {
    int N, C;
    
    while(cin >> N >> C) {
        SegmentTree segt(N);
        for (int i = 0; i < N; i++) {
            double l;
            cin >> l;
            segt.update(i, l);
        }
        vector<double> prv(N, M_PI);
    
        for (int i = 0; i < C; i++) {
            int s, a;
            cin >> s >> a;
    
            segt.change(s, (a / 360.0 * 2 * M_PI) - prv[s]);
            prv[s] = a / 360.0 * 2 * M_PI;
            printf("%.2f %.2f\n", segt.x[0], segt.y[0]);
        }
        cout << endl;
    }
}