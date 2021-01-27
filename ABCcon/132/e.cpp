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
    int n, m; cin >> n >> m;
    vector<vector<int>> edge(n);
    rep(i,m){
        int u, v; cin >> u >> v;
        u--;v--;
        edge[u].push_back(v);
    }
    int s, t; cin >> s >> t;
    s--;t--;

    //bfs
    queue<P> q;
    vector<vector<int>> dist_mod3(n, vector<int>(3, -1));
    q.push(make_pair(s,0));
    dist_mod3[s][0] = 0;
    while(!q.empty()){
        P pp = q.front();
        int p = pp.first;
        int p_mod3 = pp.second;
        q.pop();
        for(auto c:edge[p]){
            if(dist_mod3[c][(p_mod3+1)%3]!=-1)continue;
            q.push(make_pair(c, (p_mod3+1)%3));
            dist_mod3[c][(p_mod3+1)%3] = dist_mod3[p][p_mod3]+1;
        }
    }
    if(dist_mod3[t][0]==-1)
        cout << -1 << endl;
    else
        cout << dist_mod3[t][0]/3 << endl;
    return 0;
}