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

ll dp[3030][3030];

int main() {
    int n; cin >> n;
    ll a[n];
    rep(i,n) cin >> a[i];
    rep(i, n) dp[i][i+1] = a[i];

    for(int width = 1;width<=n;width++){
        for(int l=0;l+width<=n;l++){
            int r = l+width;
            if(width%2==n%2)
                dp[l][r] = max(dp[l+1][r] + a[l],
                               dp[l][r-1] + a[r-1]);
            else
                dp[l][r] = min(dp[l+1][r]-a[l],
                               dp[l][r-1]-a[r-1]);
        }
    }
    cout << dp[0][n] << endl;
    return 0;
}