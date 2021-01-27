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
    int n, m;
    cin >> n >> m;
    int a[n];
    rep(i,n) cin >> a[i];
    int s_mod[n+1];
    s_mod[0] = 0;
    rep(i,n) s_mod[i+1] = (s_mod[i] + a[i]) % m;
    map<int, int> mod_count;
    rep(i,n+1) mod_count[s_mod[i]]++;
    ll ans = 0;
    rep(i, n+1){
        int now_mod = s_mod[i];
        mod_count[now_mod]--;
        ans += mod_count[now_mod];
    }
    cout << ans << endl;
    return 0;
}