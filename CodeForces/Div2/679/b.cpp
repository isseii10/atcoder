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
    int t; cin >> t;
    while(t--){
        int n, m; cin >> n >> m;
        vector<vector<int>> a(n, vector<int>(m, 0)); 
        vector<vector<int>> b(m, vector<int>(n, 0));
        rep(i,n)rep(j,m){
            cin >> a[i][j];
        }
        rep(i,m)rep(j,n){
            cin >> b[i][j];
        }
        int left_colum[n];
        rep(i,n)
            left_colum[i] = a[i][0];

        int idx[n];
        rep(i,m){
            if(find(b[i].begin(),b[i].end(),left_colum[0])==b[i].end())
                continue;
            rep(j, n){
                idx[j] = find(b[i].begin(), b[i].end(), left_colum[j])-b[i].begin();
            }
        }
        vector<vector<int>> ans(n);
        rep(i,n){
            rep(j,m){
                ans[idx[i]].push_back(a[i][j]);
            }
        }
        rep(i, n){
            rep(j,m){
                cout << ans[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}