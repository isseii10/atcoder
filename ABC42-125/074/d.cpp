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
    int n; cin >> n;
    ll a[n][n];
    ll dist[n][n];
    rep(i,n)rep(j,n) {
        cin >> a[i][j];
        dist[i][j] = a[i][j];
    }
    vector<vector<bool>> edge(n, vector<bool>(n, true));
    for (int k=0;k<n;k++){
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i != k && j != k && dist[i][j] == dist[i][k]+dist[k][j]){
                    edge[i][j] = false;
                }
                if(dist[i][j]>dist[i][k]+dist[k][j]){
                    dist[i][j] = dist[i][k]+dist[k][j];
                }
                
            }
        }
    }
    bool flag=true;
    ll ans = 0;
    rep(i,n){
        rep(j,n){
            if(a[i][j]!=dist[i][j]) {
                flag = false;
                break;
            }
            if(edge[i][j]) ans += a[i][j];
        }
        if(!flag)break;
    }
    if(flag)cout << ans / 2 << endl;
    else cout << -1 << endl;
    return 0;
}