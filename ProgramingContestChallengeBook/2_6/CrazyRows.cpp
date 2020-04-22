/*
下三角行列にするための最小の入れ替え回数
https://code.google.com/codejam/contest/204113/dashboard#s=p0
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        int N;
        cin >> N;
        vector<int> last_one(N, 0);
        for (int j = 0; j < N; j++) {
            string num;
            cin >> num;
            for (int k = N-1; k >= 0; k--) {
                if (num[k] == '1') {
                    last_one[j] = k+1;
                    break;
                }
            }
        }

        int ans = 0;
        for (int j = 1; j <= N; j++) {
            for (int k = 0; k < last_one.size(); k++) {
                if (last_one[k] <= j) {
                    ans += k;
                    last_one.erase(last_one.begin()+k);
                    break;
                }
            }
        }
        
        cout << "Case #" << i << ": " << ans << endl;
    }
}