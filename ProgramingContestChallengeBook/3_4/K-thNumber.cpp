/*
http://poj.org/problem?id=2104
セグメント木 or 平方分割、区間をソートした際にk番目の値が何か求める問題
*/
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
    int n, m;
    cin >> n >> m;
    int bucket_num = sqrt((double)n);
    vector<int> A(n);
    for (int i = 0; i < n; i++)
        cin >> A[i];
    
    vector<vector<int>> buckets(n/bucket_num + (n%bucket_num != 0 ? 1 : 0));
    vector<int> sortedA(n);
    for (int i = 0; i < n; i++) {
        buckets[i / bucket_num].push_back(A[i]);
        sortedA[i] = A[i];
    }
    sort(sortedA.begin(), sortedA.end());
    for (int i = 0; i < n / bucket_num; i++)
        sort(buckets[i].begin(), buckets[i].end());
    
    for (int i = 0; i < m; i++) {
        int l, r, k;
        cin >> l >> r >> k;
        l--;

        int lb = -1, ub = n-1;
        while (ub - lb > 1) {
            int md = (lb+ub) / 2;
            int x = sortedA[md];
            int tl = l, tr = r, c = 0;

            while (tl < tr && tl & bucket_num != 0)
                if (A[tl++] <= x)
                    c++;
            while (tl < tr && tr & bucket_num != 0)
                if (A[--tr] <= x)
                    c++;
            
            while (tl < tr) {
                int b = tl / bucket_num;
                c += upper_bound(buckets[b].begin(), buckets[b].end(), x) - buckets[b].begin();
                tl += bucket_num;
            }

            if (c >= k)
                ub = md;
            else
                lb = md;
        }
        cout << sortedA[ub] << endl;
    }
}