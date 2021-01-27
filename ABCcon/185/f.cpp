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

using S = ll;
using F = ll;

S op(S x, S y)
{
    return x ^ y;
}

S e()
{
    return 0;
}

F id()
{
    return 0;
}

S mapping(F f, S x)
{
    return f ^ x;
}

F composition(F f, F g) //fが後
{
    return f ^ g;
}


using lazy_seg = atcoder::lazy_segtree<S, op, e, F, mapping, composition, id>;

int main() {
    int n, q; cin >> n >> q;
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    lazy_seg seg(a);

    rep(i,q){
        int t; cin >> t;
        ll x, y; cin >> x >> y;
        if(t==1){
            seg.apply(x-1, y);
        }
        else{
            cout << seg.prod(x-1, y) << endl;
        }
    }

    return 0;
}