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
    int a[n];
    rep(i,n) cin >> a[i];
    sort(a, a+n);
    int gcd_a = a[0];
    rep(i,n-1){
        gcd_a = gcd(gcd_a, a[i+1]);
    }
    cout << gcd_a << endl;
    return 0;
}