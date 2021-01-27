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

ll dp[110][110][305];

int main() {
    ll n, w;
    cin >> n >> w;
    vector<pair<ll,ll>> wv(n);
    rep(i,n) cin >> wv[i].first >> wv[i].second;
    ll w0 = wv[0].first;
    for(int i=0;i<n;i++){
        ll wi = wv[i].first - w0;
        ll vi = wv[i].second;
        
        for(int j=0;j<=n;j++){
            for(int k=0;k<=300;k++){
                dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k]);
                dp[i+1][j+1][k+wi] = max(dp[i+1][j+1][k+wi],dp[i][j][k] + vi);
            }
        }
    }
    ll ans = 0;
    rep(j,n+1){
        rep(k,301){
            if(j*w0+k <= w)
                ans = max(ans, dp[n][j][k]);
        }
    }
    cout << ans << endl;
    return 0;

}
