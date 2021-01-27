#include <bits/stdc++.h>
//#include <atcoder/all>
#define REP(i, n) for (int i=0; i < (n); i++)
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

class SCC{
private:
    vector<vector<int> > gg, rg;
    vector<int> order, comp;
    vector<bool> used;
    vector<vector<int> > ng, vs;

    int n, nn;
public:
    SCC(){}
    SCC(int v) : gg(v), rg(v), comp(v, -1), used(v, 0), n(v){}

    void add_edge(int x, int y){
        gg[x].push_back(y);
        rg[y].push_back(x);
    }

    int operator[](int k){
        return comp[k];
    }

    void dfs(int v){
        used[v] = true;
        REP(i, gg[v].size()){
            if(!used[gg[v][i]]) dfs(gg[v][i]);
        }
        order.push_back(v);
    }

    void rdfs(int v, int k){
        used[v] = true;
        comp[v] = k;
        REP(i, rg[v].size()){
            if(!used[rg[v][i]]) rdfs(rg[v][i], k);
        }
    }

    int build(){
        REP(i, n){
            if(!used[i]) dfs(i);
        }
        fill(used.begin(), used.end(), 0);
        int k = 0;
        for(int i = order.size()-1;i >= 0;i--){
            if(!used[order[i]]) rdfs(order[i], k++);
        }
        nn = k;

        //---------それぞれの強連結成分に含まれる頂点の番号----------
        vs.resize(k, vector<int>());

        REP(i, n)
            vs[comp[i]].push_back(i);
        //-----------------------------------------------------------

        //---------強連結成分をまとめた後のNew Graph!----------------
        ng.resize(k, vector<int>());
        REP(i, n){
            REP(j, gg[i].size()){
                if(comp[i] != comp[gg[i][j]])
                    ng[comp[i]].push_back(comp[gg[i][j]]);
            }
        }
        REP(i, nn){
            sort(ng[i].begin(), ng[i].end());
            ng[i].erase(unique(ng[i].begin(), ng[i].end()), ng[i].end());
        }
        //------------------------------------------------------------
        return k;
    }
    
    int size(){
        return nn;
    }

    vector<vector<int> > graph(){
        return ng;
    }

    vector<int> vertices(int v){
        return vs[v];
    }
};

    

int main() {
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        string s; cin >> s;
        SCC scc = SCC(n);
        REP(i,n){
            if(s[i]=='>'){
                scc.add_edge(i % n, (i+1)%n);
            }
            else if(s[i]=='<'){
                scc.add_edge((i+1)%n, i%n);

            }
            else{
                scc.add_edge(i % n, (i+1)%n);
                scc.add_edge((i+1)%n, i%n);
            }
        }
        scc.build();
        int ans = 0;
        cout << scc.size() << endl;
        cout << endl;
    }
    return 0;
}