
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

ll dp[110][100010];
ll dp_sum[110][100010];

int main() {
    int n, k;
    cin >> n >> k;
    int a[n];
    rep(i,n) cin >> a[i];

    dp[0][0] = 1;
    rep(j,k+1) dp_sum[0][j] = 1;

    for(int i = 0;i<n;i++){
        for(int j=0;j<=k;j++){
            if(j-a[i]-1>=0){
                dp[i+1][j] += dp_sum[i][j] - dp_sum[i][j-a[i]-1];
                dp[i+1][j] += MOD;
                dp[i+1][j] %= MOD;
            }
            else{
                dp[i+1][j] += dp_sum[i][j];
                dp[i+1][j] %= MOD;
            }
            if(j==0){
                dp_sum[i+1][j] = dp[i+1][j];
                dp_sum[i+1][j] %= MOD;
            }
            else{
                dp_sum[i+1][j] = dp_sum[i+1][j-1] + dp[i+1][j];
                dp_sum[i+1][j] %= MOD;
            }
        }
    }
    cout << dp[n][k] << endl;
    return 0;
}