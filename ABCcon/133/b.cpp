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
    int n, d; cin >> n >> d;
    vector<vector<int>> xs(n);
    rep(i,n)rep(j,d) {
        int x; cin >> x;
        xs[i].push_back(x);
    }
    int ans=0;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            int res = 0;
            for(int d_=0;d_<d;d_++){
                res += (xs[i][d_]-xs[j][d_])*(xs[i][d_]-xs[j][d_]);
            }
            double res2 = sqrt(res);
            if(res2 == (int)res2) ans++;
        }
    }
    cout << ans << endl;
    return 0;
}