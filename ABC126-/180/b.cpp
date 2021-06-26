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

ll man(vector<ll> a, int n){
    ll res = 0;
    rep(i,n){
        res += abs(a[i]);
    }
    return res;
}

double yu(vector<ll> b, int n){
    ll res = 0;
    rep(i,n){
        res += b[i]*b[i];
    }
    double res2 = sqrt(res);
    return res2;
}

ll tye(vector<ll> c, int n){
    ll res = 0;
    rep(i,n){
        res = max(res, abs(c[i]));
    }
    return res;
}

int main() {
    int n; cin >> n;
    vector<ll> x(n);
    rep(i,n) cin >> x[i];

    cout << man(x, n) << endl;
    cout << setprecision(15) << yu(x, n) << endl;
    cout << tye(x, n) << endl;

    return 0;
}