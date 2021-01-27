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

double dp[3300][3300];

int main() {
    int n; cin >> n;
    double p[n];
    rep(i,n) cin >> p[i];
    dp[0][0] = 1;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            dp[i+1][j+1] += dp[i][j]*p[i];
            dp[i+1][j] += dp[i][j]*(1-p[i]);
        }
    }
    
    double ans = 0;
    for(int j=(n-1)/2+1;j<=n;j++){
        ans += dp[n][j];
    }
    cout << setprecision(15) << ans << endl;
    return 0;
}