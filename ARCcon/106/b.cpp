#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
using namespace atcoder;
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
    int n, m; cin >> n >> m;
    ll a[n], b[n];
    ll sum_a, sum_b;
    sum_a = 0;
    sum_b = 0;
    rep(i,n) {
        cin >> a[i];
        sum_a += a[i];
    }
    rep(j,n) {
        cin >> b[j];
        sum_b += b[j];
    }

    if(sum_a!=sum_b){
        cout << "No" << endl;
        return 0;
    }

    dsu uf(n);
    rep(i,m){
        int c, d; cin >> c >> d;
        c--;d--;
        uf.merge(c, d);
    }
    vector<ll> sa(n, 0);
    rep(i,n) sa[i] = b[i] - a[i];
    bool out_flag = false;
    for(auto vs : uf.groups()){
        ll res = 0;
        for(auto v : vs){
            res += sa[v];
        }
        if(res != 0)
            out_flag = true;
        
        if(out_flag)break;
    }
    if(out_flag)
        cout << "No" << endl;
    else
        cout << "Yes" << endl;
    return 0;
}