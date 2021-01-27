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

int main() {
    int n, K; cin >> n >> K;
    int a[n][n];
    rep(i,n)rep(j,n) cin >> a[i][j];

    set<P> tate_set;
    set<P> yoko_set;

    for(int k=0;k<n;k++){ //行指定
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(a[k][i]+a[k][j] > K)
                    yoko_set.insert(make_pair(i,j));
            }
        }
    }
    for(int k=0;k<n;k++){ //retu指定
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(a[i][k]+a[j][k] > K)
                    tate_set.insert(make_pair(i,j));
            }
        }
    }
    ll tate_sz = tate_set.size();
    ll yoko_sz = yoko_set.size();

    ll tate_edge = n*(n-1)/2;
    ll yoko_edge = n*(n-1)/2;
    tate_edge -= tate_sz;
    yoko_edge -= yoko_sz;
    cout << tate_edge << endl;
    cout << yoko_edge << endl;

    ll ans  = 1;
    for(int i=1;i<=tate_edge;i++){
        ans = ans*i % MOD2;
    }
    for(int i=1;i<=yoko_edge;i++){
        ans = ans*i % MOD2;
    }
    cout << ans << endl;
    return 0;
}