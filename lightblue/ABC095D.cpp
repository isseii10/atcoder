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
    ll n, c;
    cin >> n >> c;
    vector<pair<ll, ll>> xv(n);
    rep(i,n) cin >> xv[i].first >> xv[i].second;
    ll s[n+1], rs[n+1];
    s[0] = 0;
    rs[0] = 0;
    rep(i,n) {
        s[i+1] = s[i] + xv[i].second;
        rs[i+1] = rs[i] + xv[n-1-i].second;
    }
    ll max_[n+1], max_r[n+1];
    max_[0] = 0;
    max_r[0] = 0;
    rep(i,n){
        max_[i+1] = max(max_[i], s[i+1] - xv[i].first);
        max_r[i+1] = max(max_r[i], rs[i+1]-(c-xv[n-1-i].first));
    }
    ll ans = 0;
    for(int take_tokei = 1; take_tokei<=n;take_tokei++){
        ll res = s[take_tokei] - xv[take_tokei-1].first;
        if(max_r[n-take_tokei]>xv[take_tokei-1].first){
            res += max_r[n-take_tokei] - xv[take_tokei-1].first;
        }
        ans = max(ans, res);
    }
    for(int take_hantokei = 1;take_hantokei<=n;take_hantokei++){
        ll res = rs[take_hantokei] - (c-xv[n-take_hantokei].first);
        if(max_[n-take_hantokei] > c - xv[n-take_hantokei].first){
            res += max_[n-take_hantokei] - (c-xv[n-take_hantokei].first);
        }
        ans = max(ans, res);
    };
    cout << ans << endl;
    return 0;
}