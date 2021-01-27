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
    int t; cin >> t;
    while (t--)
    {
        int n, k; cin >> n >> k;
        ll a[n];
        rep(i,n) cin >> a[i];
        sort(a, a+n);
        ll ans = a[n-1];
        rep(i,k){
            if(n-2-i>=0)
                ans += a[n-2-i];
            else
                break;
        }
        cout << ans << endl;

    }
    
    return 0;
}