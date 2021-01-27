#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
//using namespace atcoder;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> P;
const int INF = 1 << 30;
const ll LINF = 1LL << 61;
const int NIL = -1;
const int MAX = 10000;
const int MOD = 1000000007;
const int MOD2 = 998244353; 
const double pi = 3.141592653589;

// mod. m での a の逆元 a^{-1} を計算する
long long modinv(long long a, long long m = MOD2) {
    long long b = m, u = 1, v = 0;
    while (b) {
        long long t = a / b;
        a -= t * b; swap(a, b);
        u -= t * v; swap(u, v);
    }
    u %= m;
    if (u < 0) u += m;
    return u;
}
int main(){
    ll a, b, c; cin >> a >> b >> c;
    ll ans_a = (a*(a+1) % MOD2) * modinv(2) % MOD2;
    ll ans_b = (b*(b+1) % MOD2) * modinv(2) % MOD2;
    ll ans_c = (c*(c+1) % MOD2) * modinv(2) % MOD2;
    ll ans = (ans_a * ans_b) % MOD2 * ans_c % MOD2;
    cout << ans << endl;
    return 0;
}