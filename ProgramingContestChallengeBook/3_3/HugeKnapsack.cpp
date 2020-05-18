/*
オリジナル問題
半分全列挙、重さの限界値がとても大きい(DPだと配列に収まらない)場合のナップサック問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const ll INF = 1e16;
const int max_n = 40;
int n;
ll w[max_n], v[max_n];
ll W;

pair<ll, ll> ps[1 << max_n / 2]; //前半部分の重みと価値の組み合わせ

int main() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> w[i];
    for (int i = 0; i < n; i++)
        cin >> v[i];
    cin >> W;

    // 品物の前半部分の全列挙
    int n2 = n / 2;
    for (int i = 0; i < 1 << n2; i++) {
        ll sw = 0, sv = 0;
        for (int j = 0; j < n2; j++) {
            if (i >> j & 1) {
                sw += w[j];
                sv += v[j];
            }
        }
        ps[i] = make_pair(sw, sv);
    }

    sort(ps, ps + (1 << n2));
    // 重み順に昇順ソートされており、価値が一個前のものより軽いなら使わないため削除
    int m = 1;
    for (int i = 1; i < 1 << n2; i++) {
        if (ps[m-1].second < ps[i].second) {
            ps[m++] = ps[i];
        }
    }

    // 後ろ半分を全列挙
    ll res = 0;
    for (int i = 0; i < 1 << (n-n2); i++) {
        ll sw = 0, sv = 0;
        for (int j = 0; j < n-n2; j++) {
            if (i >> j & 1) {
                sw += w[n2+j];
                sv += v[n2+j];
            }
        }
        if (sw <= W) {
            // 重さW-sw以上かつ価値INF以上の要素の１個前の要素、つまり重さW-swの中で価値最大のものを探索
            ll tv = (lower_bound(ps, ps+m, make_pair(W-sw, INF))-1)->second;
            res = max(res, sv+tv);
        }
    }

    cout << res << endl;
}