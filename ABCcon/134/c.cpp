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
    rep(i,n) {
        cin >> a[i];
        b[i] = a[i];
    }
    sort(b, b+n);
    int max_a = b[n-1];
    int max_a2 = b[n-2];

    rep(i,n){
        if(a[i] == max_a) cout << max_a2 << endl;
        else cout << max_a << endl;
    }
    return 0;
}