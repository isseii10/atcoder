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
    int n;
    cin >> n;
    int a[2][n];
    rep(i,2)rep(j,n) cin >> a[i][j];

    int ans = 0;
    for(int i=0;i<n;i++){
        int res = 0;
        for(int j=0;j<n;j++){
            if(j<=i) res += a[0][j];
            if(j>=i) res += a[1][j];
        }
        ans = max(ans, res);
    }
    cout << ans << endl;

    return 0;
}