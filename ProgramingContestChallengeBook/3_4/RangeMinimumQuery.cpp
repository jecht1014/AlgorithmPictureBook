/*
Range Minimu Queryの実装
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll INF = 1e15;

struct RMQ {
    int leaf_node_num;
    vector<ll> node_value;
    
    RMQ(int input_num) {
        leaf_node_num = 1;
        while (leaf_node_num < input_num)
            leaf_node_num *= 2;
        
        for (int i = 0; i < 2*leaf_node_num-1; i++)
            node_value.push_back(INF);
    }

    // k番目の値をaに変更
    void update(int k, ll a) {
        k += leaf_node_num-1;
        node_value[k] = a;

        // rootに向かって遡って更新
        while (k > 0) {
            k = (k-1) / 2;
            node_value[k] = min(node_value[k*2+1], node_value[k*2+2]);
        }
    }

    // 区間[a, b)の最小値を求める
    // 後ろの3つの引数は計算用の引数
    // kは節点番号で最初はrootを呼び出すため0
    // l, rは節点kが[l, r)に対応していることを示す
    // よって最初はquery(a, b, 0, 0, n)で呼び出す
    ll query(int a, int b, int k=0, int l=0, int r=-1) {
        // 最初のクエリのとき
        if (r == -1)
            r = leaf_node_num;
        // [a, b)と[r, l)が一切重なっていないとき
        if (r <= a || b <= l)
            return INF;
        // [r, l)を[a, b)がすべて含んでいるとき
        if (a <= l && r <= b)
            return node_value[k];
        else {
            // そうでないときは子ノードの最小値
            ll vl = query(a, b, k*2 + 1, l, (l+r) / 2);
            ll vr = query(a, b, k*2 + 2, (l+r) / 2, r);
            return min(vl, vr);
        }
    }
};

int main() {
    RMQ rmq(8);
    rmq.update(0, 5);
    rmq.update(1, 3);
    rmq.update(2, 7);
    rmq.update(3, 9);
    rmq.update(4, 6);
    rmq.update(5, 4);
    rmq.update(6, 1);
    rmq.update(7, 2);
    for (int i = 0; i < 15; i++)
        cout << rmq.node_value[i] << " ";
}