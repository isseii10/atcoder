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
    ll a[n];
    rep(i,n) cin >> a[i];

    vector<vector<ll>> dp(n+1, vector<ll>(n+1, LINF));
    rep(i, n){
        dp[i][i+1] = 0; //この区間内にはスライム１匹しかいないのでコストはかからない
    }
    
    ll sum_a[n];
    sum_a[0] = a[0];
    for(int i=1;i<n;i++){
        sum_a[i] = sum_a[i-1] + a[i];
    }

    for(int w=1;w<=n;w++){ //width
        for(int l=0;l+w<=n;l++){
            int r = l+w;
            for(int m=l+1;m<r;m++){
                if(l-1>=0)
                    dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r] + sum_a[r-1] - sum_a[l-1]);
                else
                    dp[l][r] = min(dp[l][r], dp[l][m] + dp[m][r] + sum_a[r-1]);
                
            }
        }
    }
    cout << dp[0][n] << endl;
    return 0;
}