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

bool from_1[3000];
bool from_n[3000];

void dfs(int p, vector<vector<int>> &edges){ //アドレス演算子で渡した(参照渡し）ほうが早いしメモリも節約されている。
    from_1[p] = true;
    for(auto c : edges[p]){
        if(from_1[c])continue;
        from_1[c] = true;
        dfs(c, edges);
    }
    return;
}

void rdfs(int p, vector<vector<int>> &redges){
    from_n[p] = true;
    for(auto c : redges[p]){
        if(from_n[c])continue;
        from_n[c] = true;
        rdfs(c, redges);
    }
    return;
}

struct edge{
    int from;
    int to;
    int cost;
};

int main() {
    int n, m, pena; cin >> n >> m >> pena;
    vector<edge> edges_list; //辺集合
    vector<vector<int>> edges(n);
    vector<vector<int>> redges(n);
    rep(i,m){
        int a, b, c;
        cin >> a >> b >> c;
        a--;b--;
        edge add_edge;
        add_edge.from = a;
        add_edge.to = b;
        add_edge.cost = -(c-pena);
        edges_list.push_back(add_edge);
        edges[a].push_back(b);
        redges[b].push_back(a);
    }
    
    dfs(0, edges);
    rdfs(n-1, redges);

    //bellman-ford
    int d[n];//始点からのコスト
    fill(d, d+n, INF);
    d[0] = 0; //始点は０
    bool negative_loop_flag = false;
    for(int i=0;i<n;i++){
        for(auto e : edges_list){
            if(!(from_1[e.to] && from_n[e.to]))continue;
            if(!(from_1[e.from] && from_n[e.from]))continue;
            
            if(d[e.to] > d[e.from]+e.cost){
                d[e.to] = d[e.from] + e.cost;
                if(i==n-1){
                    negative_loop_flag = true;
                    break;
                }
            }
        }
    }
    if(negative_loop_flag){
        cout << -1 << endl;
    }
    else
        cout << max(0, -d[n-1]) << endl;
    return 0;
}