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
    int n, m;
    cin >> n >> m;
    ll l; cin >> l;
    vector<vector<ll>> edges(n, vector<ll>(n, LINF));
    rep(i,m){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        if(c>l)continue;
        a--;b--;
        edges[a][b] = c;
        edges[b][a] = c;
    }
    vector<vector<ll>> dist(n, vector<ll>(n, LINF));
    rep(i,n)rep(j,n){
        if(i==j)dist[i][j] = 0;
        if(edges[i][j]!= LINF)
            dist[i][j] = edges[i][j]; 
    }

    for(int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(dist[i][j] > dist[i][k] + dist[k][j]){
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    vector<vector<ll>> charge(n, vector<ll>(n, LINF));
    rep(i,n)rep(j,n){
        if(i==j)charge[i][j] = 0;
        if(dist[i][j]<=l) charge[i][j] = 1;
    }
    rep(k,n)rep(i,n)rep(j,n){
        if(charge[i][j] > charge[i][k] + charge[k][j]){
            charge[i][j] = charge[i][k] + charge[k][j];
        }
    }

    int q; cin >> q;
    int s[q], t[q];
    rep(i,q){
        cin >> s[i] >> t[i];
        s[i]--;t[i]--;
    }
    rep(i,q){
        if(charge[s[i]][t[i]]==LINF) cout << -1 << endl;
        else cout << charge[s[i]][t[i]]-1 << endl;
    }

    return 0;
}