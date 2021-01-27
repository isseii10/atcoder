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
    int n;
    cin >> n;
    ll a[n], x[n];
    rep(i,n){
        cin >> a[i];
        a[i] -= i+1;
        x[i] = a[i];
    }
    sort(x, x+n);
    
    ll ans = 0;
    if (n%2==1) {
        ll b = x[n/2];
        rep(i,n) ans += abs(a[i]-b);
    }
    else{
        ll b1, b2;
        b1 = x[n/2 -1];
        b2 = x[n/2];
        ll res1 = 0, res2 = 0;
        rep(i,n) res1 += abs(a[i]-b1);
        rep(i,n) res2 += abs(a[i]-b2);
        ans = min(res1, res2);
    }
    cout << ans << endl;

    return 0;
}