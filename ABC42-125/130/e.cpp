#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
using namespace atcoder;
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
using mint = modint1000000007;

int main() {
    int n, m; cin >> n >> m;
    int s[n], t[m];
    rep(i,n) cin >> s[i];
    rep(i,m) cin >> t[i];
    vector<vector<mint>> dp(n+1, vector<mint>(m+1, 0));
    dp[0][0] = 1;
    for(int i=0;i<=n;i++){
        for(int j=0;j<=m;j++){
            if(i-1>=0 && j-1>=0 && s[i-1]==t[j-1])dp[i][j] += dp[i-1][j-1];
            if(i-1>=0) dp[i][j] += dp[i-1][j];
            if(j-1>=0) dp[i][j] += dp[i][j-1];
            if(i-1>=0 && j-1>=0) dp[i][j] -= dp[i-1][j-1];
        }

    }
    cout << dp[n][m].val() << endl;
    return 0;
}