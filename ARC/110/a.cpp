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

ll lcm(ll x, ll y){
    return x / gcd(x, y) * y;
}

int main() {
    ll n; cin >> n;
    vector<ll> prime(31, 0);
    ll ans = 1;
    for(ll i=2;i<=n;i++){
        ans = lcm(ans, i);
    }
    ans++;
    
    cout << ans << endl;
    return 0;
}