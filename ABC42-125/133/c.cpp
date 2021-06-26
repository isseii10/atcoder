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
    ll l, r; cin >> l >> r;
    ll ans = LINF;
    if(r-l + 1 >= 2019) ans = 0;
    else {
        for(ll i=l;i<r;i++){
            for(ll j=i+1;j<=r;j++){
                ll res = (i*j)%2019;
                ans = min(ans, res);
            }
        }
    }
    cout << ans << endl;
    return 0;
}