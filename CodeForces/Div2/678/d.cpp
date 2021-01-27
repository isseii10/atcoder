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

vector<vector<int>> edges(200200);
ll a[200200];
ll dp[200200];
ll child_count[200200];
void dfs(int p, int pp=-1){
    dp[p] = a[p];
    child_count[p] = edges[p].size();
    for(auto c : edges[p]){
        if(pp==c)continue;
        dfs(c, p);
        dp[p] = max(dp[p], a[p]/child_count[p] + dp[c]);
    }
}

int main() {
    int n; cin >> n;
    rep(i,n-1){
        int p; cin >> p;
        p--;
        edges[p].push_back(i+1);
    }
    rep(i,n) cin >> a[i];

    dfs(0);
    cout << dp[0] << endl;

    return 0;
}