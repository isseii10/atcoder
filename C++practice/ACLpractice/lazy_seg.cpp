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

struct S{
    ll value;
    ll cnt0;
    ll cnt1;
};

using F = int;

S op(S x, S y)
{
    return {x.value+y.value+x.cnt1*y.cnt0, x.cnt0+y.cnt0, x.cnt1+y.cnt1};
}

S e()
{
    return {0,0,0};
}

F id()
{
    return 0;
}

S mapping(F f, S x)
{
    if(f!=0)return {x.cnt0*x.cnt1 - x.value, x.cnt1, x.cnt0};
    else return x;
}

F composition(F f, F g) //fが後
{
    return f^g;
}


using lazy_seg = atcoder::lazy_segtree<S, op, e, F, mapping, composition, id>;     
int main() {
    int n, q; cin >> n >> q;
    vector<S> v(n);
    rep(i,n){
        int a;
        cin >> a;
        if(a==0)v[i] = {0, 1, 0};
        else v[i] = {0, 0, 1};
    }
    lazy_seg seg(v);

    rep(i, q){
        int t, l, r; cin >> t >> l >> r;
        if (t==1){
            seg.apply(l-1, r, 1);
        }
        else cout << seg.prod(l-1, r).value << endl;
    }
    return 0;
}