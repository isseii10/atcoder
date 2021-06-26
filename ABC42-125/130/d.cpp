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
    ll n, k;
    cin >> n >> k;
    ll a[n];
    rep(i, n) cin >> a[i];
    vector<ll> a_s(n+1, 0);
    rep(i, n) a_s[i+1] = a_s[i] + a[i];
    ll ans = 0;
    for (int i = 0;i < n;i++){
        ll idx;
        auto it = lower_bound(a_s.begin(), a_s.end(), k+a_s[i]);
        idx = it - a_s.begin();
        ans += n - idx + 1;
    }
    cout << ans << endl;
}