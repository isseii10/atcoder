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
    int a[n+2];
    rep(i,n) cin >> a[i+1];
    a[0] = 0;
    a[n+1] = 0;
    vector<int> ans(n, 0);
    rep(i,n) ans[i] += abs(a[i] - a[i+2]) - abs(a[i] - a[i+1]) - abs(a[i+1] - a[i+2]);
    
    int s = 0;
    for(int i=1;i<=n+1;i++) s += abs(a[i-1] - a[i]);
    rep(i,n) cout << s + ans[i] << endl;
    return 0;
}