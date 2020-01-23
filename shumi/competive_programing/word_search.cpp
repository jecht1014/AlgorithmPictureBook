#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<long long> create_table(string pattern) {
    vector<long long> table(pattern.size()+1, 0);
    
    long long j = 0;
    for (long long i = 1; i < pattern.size(); i++) {
        if (pattern[i] == pattern[j])
            table[i] = j++;
        else {
            table[i] = j;
            j = 0;
        }
    }
    table[pattern.size()] = j;

    return table;
}

// KMPサーチ
vector<long long> kmp_search(string target, string pattern) {
    vector<long long> table = create_table(pattern);
    
    vector<long long> result;
    long long p = 0;
    for (long long i = 0; i < target.size(); i++) {
        if (target[i] == pattern[p])
            p++;
        else if (p != 0 && target[i] != pattern[p]) {
            p = table[p];
            i--;
        }
        
        if (p == pattern.size()) {
            result.push_back((i+1)-p);
            p = table[p];
        }
    }
    
    return result;
}

int main() {
    string target = "AABABBABABCAB";
    string pattern = "ABABC";
    vector<ll> kmp = kmp_search(target, pattern);
}