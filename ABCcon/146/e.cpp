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
    ll n, k; cin >> n >> k;
    ll a[n];
    rep(i,n) cin >> a[i];
    ll a_mod[n];
    for(int i=0; i<n;i++){
        a_mod[i] = a[i] % k;
    }
    rep(i,n) cout << a_mod[i] << " ";
    cout << endl;


    return 0;
}