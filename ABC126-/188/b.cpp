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
    int a[n], b[n];
    rep(i,n) cin >> a[i];
    rep(i,n) cin >> b[i];
    int ans = 0;
    rep(i,n){
        ans += a[i]*b[i];
    }
    if(ans) cout << "No" << endl;
    else cout << "Yes" << endl;
    return 0;
}