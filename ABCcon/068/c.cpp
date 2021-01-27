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
    vector<vector<int>> edges(n);
    rep(i,m){
        int a, b; cin >> a >> b;
        a--; b--;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    //bfs
    queue<int> q;
    vector<int> dist(n, -1);
    q.push(0);
    dist[0] = 0;
    while (!q.empty()){
        int p = q.front();
        q.pop();
        for(auto c : edges[p]){
            if(dist[c]!=-1)continue;
            dist[c] = dist[p] + 1;
            q.push(c);
        }
    }
    if (dist[n-1] == 2) cout << "POSSIBLE" << endl;
    else cout << "IMPOSSIBLE" << endl;
    return 0;
}