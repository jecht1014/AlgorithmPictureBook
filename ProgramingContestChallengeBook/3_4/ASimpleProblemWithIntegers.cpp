/*
http://poj.org/problem?id=3468
セグメント木 or BIT、区間に整数を加える処理と、区間の和を計算する処理する問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

struct SegmentTree {
    int leaf_node_num;
    vector<ll> alldata, data;
    
    SegmentTree(int input_num) {
        leaf_node_num = 1;
        while (leaf_node_num < input_num)
            leaf_node_num *= 2;
        
        for (int i = 0; i < 2*leaf_node_num-1; i++) {
            alldata.push_back(0);
            data.push_back(0);
        }
    }

    // 区間[a, b)にxを追加
    void add(ll x, int a, int b, int l=0, int r=-1, int k=0) {
        if (r == -1)
            r = leaf_node_num;
        if (a <= l && r <= b) {
            alldata[k] += x;
        }
        else if (l < b && a < r) {
            data[k] += (min(b, r) - max(a, l)) * x;
            add(x, a, b, l, (l+r)/2, k*2+1);
            add(x, a, b, (l+r)/2, r, k*2+2);
        }
    }

    // 区間[a,b)の和
    ll sum(int a, int b, int l=0, int r=-1, int k=0) {
        if (r == -1)
            r = leaf_node_num;
        
        if (b <= l || r <= a)
            return 0;
        else if (a <= l && r <= b)
            return (r-l) * alldata[k] + data[k];
        else {
            ll res = (min(b, r) - max(a, l)) * alldata[k];
            res += sum(a, b, l, (l+r)/2, k*2+1);
            res += sum(a, b, (l+r)/2, r, k*2+2);
            return res;
        }
    }
};

int main() {
    int N, Q;
    cin >> N >> Q;
    SegmentTree segt(N);
    for (int i = 0; i < N; i++) {
        ll A;
        cin >> A;
        segt.add(A, i, i+1);
    }
    
    for (int i = 0; i < Q; i++) {
        char C;
        cin >> C;
        if (C == 'Q') {
            int a, b;
            cin >> a >> b;
            cout << segt.sum(a-1, b) << endl;
        }
        else {
            int a, b;
            ll c;
            cin >> a >> b >> c;
            segt.add(c, a-1, b);
        }
    }
}