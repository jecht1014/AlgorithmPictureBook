#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

// 最大公約数
ll gcd(ll a, ll b) {
    if (a < b) {
        ll tmp = a;
        a = b;
        b = tmp;
    }
    
    ll r = a % b;
    while(r != 0) {
        a = b;
        b = r;
        r = a % b;
    }
    return b;
}

// 最小公倍数
ll lcm(ll a, ll b) {
    return a * b / gcd(a, b);
}

// 拡張ユークリッド互除法(ax+by=cとなるようなx,yと最小のcを求めるプログラム)
long long extgcd(long long a, long long b, long long& x, long long& y) {
    long long c = a;
    if (b != 0) {
        c = extgcd(b, a%b, y, x);
        y -= (a / b) * x;
    }
    else {
        x = 1;
        y = 0;
    }
    return c;
}

// 素因数分解
vector<int> prime_factrization(ll n) {
    vector<int> prime_num(n+1);
    for (int i = 2; i*i <= n; i++) {
        while(n % i == 0) {
            prime_num[i]++;
            n /= i;
        }
    }
    if (n != 1)
        prime_num[n] = 1;
    return prime_num;
}

// 素数判定
bool is_prime(long long n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}

// char型からint型に変換
int ctoi(char c) {
	if (c >= '0' && c <= '9') {
		return c - '0';
	}
	return 0;
}

int main() {
    vector<int> prime_num = prime_factrization(10);
    for (int i = 0; i <= 10; i++)
        cout << prime_num[i] << " ";
}