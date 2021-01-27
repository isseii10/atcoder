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

ll op(ll x, ll y)
{
    return min(x,  y);
}

ll e()
{
    return LINF;
}

ll id()
{
    return LINF+1;
}

ll mapping(ll f, ll x) //区間内のノードの値ｘをｆに更新
{
    if(f==id())
        return x;
    else
        return f;
    ;
}

ll composition(ll f, ll g) // fが後。ｇに更新したあとにｆに更新する
{
    if(f==id())
        return g;
    else
        return f;
    
}



using lazy_seg = atcoder::lazy_segtree<ll, op, e, ll, mapping, composition, id>;

typedef struct{
    ll s;
    ll t;
    ll x;
} stx;

int main() {   
    ll n, q; cin >> n >> q;
    ll s[n], t[n], x[n], d[q];
    rep(i,n) cin >> s[i] >> t[i] >> x[i];
    rep(i,q) cin >> d[i];
    vector<ll> v(q, -1);
    lazy_seg sg(v);
    //更新順序をｘが大きいほうから更新していけば、うまくいく
    //ラムダ式でｘの降順にソート
    vector<stx> v_stx(n);
    rep(i,n) {
        v_stx[i].s = s[i];
        v_stx[i].t = t[i];
        v_stx[i].x = x[i];
    }
    sort(v_stx.begin(), v_stx.end(), [](stx a, stx b){return a.x > b.x;});

    //区間更新
    rep(i,n){
        //今セグ木にのせているのは座標圧縮（？）されたdなので、区間内にあるｄを更新する
        ll left = lower_bound(d, d+q, max(0LL, v_stx[i].s-v_stx[i].x))-d;
        ll right = lower_bound(d, d+q, max(0LL, v_stx[i].t-v_stx[i].x))-d;
        sg.apply(left, right, v_stx[i].x);
    }

    //一点取得
    //i番目にはi番目の人の情報が乗っている
    rep(i,q) cout << sg.get(i) << endl;


    return 0;
}