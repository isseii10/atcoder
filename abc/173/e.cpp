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
const double pi = 3.141592653589;

// mod. m での a の逆元 a^{-1} を計算する
long long modinv(long long a, long long m = 1000000007) {
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

int main() {
    int n, k; cin >> n >> k;
    vector<ll> a(n);
    int minus_count = 0;
    rep(i,n){
        cin >> a[i];
        if(a[i]<0) minus_count++;
    }
    sort(a.begin(), a.end());
    ll seki_a[n+1];
    seki_a[0] = 1;
    rep(i,n){
        seki_a[i+1] = seki_a[i] * a[i] % MOD;
    }
    ll ans = seki_a[n]/seki_a[n-k] % MOD;
    //cout << ans << endl;

    for(int i=0;i<=min(k, minus_count);i++){
        int left = i; //左からi個使う
        int right = n - (k-i);
        ll res = (seki_a[left]*(seki_a[n]/seki_a[right] %MOD))%MOD;
        ans = max(ans, res);
    }
    if(ans < 0) ans += MOD;
    cout << ans << endl;
    return 0;
}