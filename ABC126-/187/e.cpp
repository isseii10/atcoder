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

void dfs(int p, int pp, vector<vector<int>> &G, vector<int> &in, vector<int> &out){
    for(auto c : G[p]){
        if(pp == c)continue;
        in.push_back(c);
        dfs(c, p, G, in, out);
        out.push_back(c);
    }
}

int main() {
    int n; cin >> n;
    vector<vector<int>> edge(n);
    rep(i,n-1){
        int a, b; cin >> a >> b;
        a--;b--;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    vector<int> in;
    vector<int> out;
    in.push_back(0);
    dfs(0, -1, edge, in, out);
    for(auto node : out){
        cout << node << endl;
    }
    int q; cin >> q;
    while(q--){
        int t, e, x; cin >> t >> e >> x;
    }

    
    return 0;
}