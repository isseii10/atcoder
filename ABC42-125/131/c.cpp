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
    ll a, b, c, d;
    cin >> a >> b >> c >> d;
    ll range = b - a + 1;
    ll div_c, div_d, div_cd;
    div_c = b/c - (a-1)/c;
    div_d = b/d - (a-1)/d;
    ll lcm = c*d / gcd(c, d);
    div_cd = b/lcm - (a-1)/lcm;
    ll ans = range - div_c - div_d + div_cd;
    cout << ans << endl;
    return 0;
}