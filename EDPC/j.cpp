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

double dp[303][303][303];

int main() {
    int n; cin >> n;
    map<int, int> cnt;
    rep(i,n){
        int a;
        cin >> a;
        cnt[a]++;
    }
    for(int i=0;i<=n;i++){
        for(int j=0;j<=n;j++){
            for(int k=0;k<=n;k++){
                int sushi = i + j + k;
                if(sushi==0)continue;
                dp[i][j][k] = (double)n/sushi;
                if(i-1>=0)dp[i][j][k] += dp[i-1][j+1][k]*i/sushi;
                if(j-1>=0)dp[i][j][k] += dp[i][j-1][k+1]*j/sushi;
                if(k-1>=0)dp[i][j][k] += dp[i][j][k-1]*k/sushi;
            }
        }
    }
    cout  << setprecision(10) << dp[cnt[3]][cnt[2]][cnt[1]] << endl;

    return 0;
}