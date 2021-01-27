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
    int n, k; cin >> n >> k;
    int x[n];
    rep(i,n) cin >> x[i];
    int ans = 0;
    rep(i,n){
        if (x[i] <= k/2) ans += x[i]*2;
        else ans += abs(x[i]-k)*2;
    }
    cout << ans << endl;
    return 0;
}