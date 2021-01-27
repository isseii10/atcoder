#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
using namespace atcoder;
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

void dfs(int n, int p, int pp, vector<vector<P>> &es, vector<int> &label){
    for(auto child: es[p]){
        if(child.first == pp)continue;
        if(child.second == label[p]){
            label[child.first] = label[p] % n + 1;
        }
        else{
            label[child.first] = child.second;
        }
        dfs(n, child.first, p, es, label);
    }
}

int main() {
    int n, m; cin >> n >> m;
    vector<P> edges_list(m);
    vector<vector<P>> edges(n);
    vector<int> us, vs, cs;
    rep(i,m){
        int u, v, c;
        cin >> u >> v >> c;
        u--;v--;
        us.push_back(u);
        vs.push_back(v);
        cs.push_back(c);
        edges_list[i].first = u;
        edges_list[i].second = v;
    }
    //全域木の作成UnionFindでできる
    //全域木に使う辺の隣接リストedgesをつくる
    dsu uf(n);
    for(int i=0;i<m;i++){
        int x = edges_list[i].first;
        int y = edges_list[i].second;
        if(uf.same(x, y))continue;
        uf.merge(x, y);
        edges[x].emplace_back(y, cs[i]);
        edges[y].emplace_back(x, cs[i]);
    }

    //全域木でDFS
    vector<int> label(n, 0);
    label[0] = 1;
    dfs(n, 0, -1, edges, label);

    rep(i,n){
        cout << label[i] << endl;
    }
    return 0;
}