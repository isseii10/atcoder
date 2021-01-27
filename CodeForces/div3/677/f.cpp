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
    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> a(n, vector<int>(m));
    vector<vector<int>> sum_a(n, vector<int>(m));
    vector<vector<int>> mod_a(n, vector<int>(m));
    rep(i,n)rep(j,m) cin >> a[i][j];
    rep(i,n){
        sort(a[i].begin(), a[i].end());
        sum_a[i][0] = a[i][0];
        mod_a[i][0] = sum_a[i][0] % k;
        for(int j=1;j<m;j++){
            sum_a[i][j] = sum_a[i][j-1]+a[i][j];
            mod_a[i][j] = sum_a[i][j] % k;
        }
    }
    rep(i,n){
        for(int j=(m-1)/2+1;j<m;j++){
            
        }
    }
    return 0;
}