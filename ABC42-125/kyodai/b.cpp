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
    int n, k; cin >> n >> k;
    vector<vector<int>> v(n, vector<int>(k));
    rep(i,n)rep(j,k) cin >> v[i][j];
    vector<vector<int>> dp(n, vector<int>(k));
    fill(dp[0].begin(), dp[0].end(), 1);
    for(int i=0;i<n;i++){
        for(int j=0;j<k;j++){
            if(i!=0){
                auto it = upper_bound(v[i-1].begin(), v[i-1].end(), v[i][j]);
                if((it - v[i-1].begin()) != 0)
                    dp[i][j] = (dp[i][j] + dp[i-1][it-v[i-1].begin()-1])%MOD;
            }
            if(j!=0){
                dp[i][j] = (dp[i][j] + dp[i][j-1])%MOD;
            }
        }
    }
    cout << dp[n-1][k-1] << endl;
    return 0;
}