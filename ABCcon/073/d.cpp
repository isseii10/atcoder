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
    int n, m, R;
    cin >> n >> m >> R;
    vector<int> r(R);
    rep(i,R) {
        cin >> r[i];
        r[i]--;
    }
    vector<vector<int>> dist(n, vector<int>(n, INF));
    rep(i,m){
        int a, b, c;
        cin >> a >> b >> c;
        a--;b--;
        dist[a][b] = c;
        dist[b][a] = c;
    }
    rep(i,n) dist[i][i] = 0;

    rep(k,n){
        rep(i,n){
            rep(j,n){
                if(dist[i][k] == INF || dist[j][k] == INF)continue;
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    sort(r.begin(), r.end());
    int ans = INF;
    do{
        int res = 0;
        for(int i=0;i<R-1;i++){
            res += dist[r[i]][r[i+1]];
        }
        ans = min(ans, res);
    }while(next_permutation(r.begin(), r.end()));
    cout << ans << endl;
    return 0;
}