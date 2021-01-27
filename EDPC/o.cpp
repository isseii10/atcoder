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
    int n; cin >> n;
    int a[n][n];
    rep(i,n)rep(j,n) cin >> a[i][j];

    vector<vector<ll>> dp(n+1, vector<ll>(1<<n, 0));
    dp[0][0] = 1;
    for(int i=0;i<n;i++){
        for(int s=0;s < (1<<n);s++){
            for(int j=0;j<n;j++){
                if(dp[i][s]){ //枝かり 0のところからは集めない
                    if(((s>>j)&1)==0 && a[i][j]){ //sの配るver.
                        dp[i+1][s + (1<<j)] += dp[i][s];
                        dp[i+1][s + (1<<j)] %= MOD;
                    }
                }
            }
        }
    }
    cout << dp[n][(1<<n)-1] << endl;

    return 0;
}