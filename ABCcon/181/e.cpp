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

int main() {
    int n, m; cin >> n >> m;
    vector<ll> h(n);
    vector<ll> w(m);
    rep(i,n) cin >> h[i];
    rep(i,m) cin >> w[i];
    sort(h.begin(), h.end());
    vector<ll> sum_h(n+1, 0);
    rep(i,n){
        if(i%2==0)
            sum_h[i+1] = sum_h[i] - h[i];
        else
            sum_h[i+1] = sum_h[i] + h[i];
    }
    ll ans = LINF;
    rep(i,m){
        auto idx = lower_bound(h.begin(), h.end(), w[i]) - h.begin();
        ll res;
        if(idx%2==0)
            res = -(sum_h[n] - sum_h[idx]) + sum_h[idx] - w[i];
        else
            res = -(sum_h[n] - sum_h[idx]) + sum_h[idx] + w[i];
        
        ans = min(ans, res);
    }
    cout << ans << endl;

    return 0;
}