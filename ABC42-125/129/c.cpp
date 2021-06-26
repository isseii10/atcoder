#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;



int main() {
    int mod = 1000000007;
    int n, m;
    cin >> n >> m;
    ll dp[1000100];
    int out;
    rep(i, m){
        cin >> out;
        dp[out] = -1;
    }
    dp[0] = 1;
    for (int i=1; i <= n; i++){
        if(dp[i]==-1){
            dp[i] = 0;
            continue;
        };
        if (i==1)dp[i] = dp[i-1];
        else dp[i] = (dp[i-1] + dp[i-2])%mod;
    }
    cout << dp[n] << endl;
}