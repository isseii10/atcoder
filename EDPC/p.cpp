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

vector<ll> edges[100010];

ll dp[100010][2]; // 0:white 1:black

void dfs(ll p, ll pp = -1){
    dp[p][0] = dp[p][1] = 1;
    for(auto c: edges[p]){
        if(pp == c)continue;
        dfs(c, p);
        dp[p][0] = (dp[p][0] * (dp[c][1] + dp[c][0])%MOD)%MOD;
        dp[p][1] = 
        
        dp[p][1] * dp[c][0] % MOD;
    }
}

int main() {
    int n; cin >> n;
    rep(i,n-1){
        int x, y;
        cin >> x >> y;
        x--;y--;
        edges[x].push_back(y);
        edges[y].push_back(x);
    }
    dfs(0);
    cout << (dp[0][1] + dp[0][0])%MOD << endl;

    return 0;
}