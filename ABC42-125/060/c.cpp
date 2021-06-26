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
    ll n, t;
    cin >> n >> t;
    ll time[n];
    rep(i,n) cin >> time[i];
    ll ans = n*t;
    for(int i=1;i<n;i++){
        if (time[i]-time[i-1] < t){
            ans -= t - (time[i]-time[i-1]);
        }
    }
    cout << ans << endl;
    return 0;
}