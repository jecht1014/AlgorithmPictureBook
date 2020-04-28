/*
http://poj.org/problem?id=3320
しゃくとり法を用いてすべてを含む連続する最小のページ数の探索
Time Limit Exceeded　境界値でギリギリ実行時間が足りない？
類問であるARC022Bは成功
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int P;
    cin >> P;
    vector<int> a(P);
    set<int> all_thing;
    for (int i = 0; i < P; i++) {
        cin >> a[i];
        all_thing.insert(a[i]);
    }
    int all_thing_num = all_thing.size();

    map<int, int> count;
    int s = 0, t = 0, num = 0, ans = P+1;
    for(;;) {
        while(t < P && num < all_thing_num) {
            count[a[t]]++;
            if (count[a[t]] == 1)
                num++;
            t++;
        }

        if (num < all_thing_num)
            break;
        
        ans = min(ans, t-s);
        count[a[s]]--;
        if (count[a[s]] == 0)
            num--;
        s++;
    }

    cout << ans << endl;
}