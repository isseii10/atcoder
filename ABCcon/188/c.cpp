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

struct idx_rate{
    ll idx;
    ll rate;
    ll last_win;
};

idx_rate op(idx_rate x, idx_rate y)
{
    idx_rate winner;
    if(x.rate < y.rate){
        winner.idx = y.idx;
        winner.rate = y.rate;
        winner.last_win = x.idx;
    }
    else{
        winner.idx = x.idx;
        winner.rate = x.rate;
        winner.last_win = y.idx;
    }
    return winner;
}

idx_rate e()
{
    idx_rate e;
    e.rate = 0;
    e.idx = 0;
    e.last_win = -1;
    return e;
}

int main() {
    int n; cin >> n;
    vector<idx_rate> a(1<<n);
    rep(i, (1<<n)){
        cin >> a[i].rate;
        a[i].idx = i+1;
        a[i].last_win = -1;
    }
    segtree<idx_rate, op, e> st(a);
    idx_rate winner = st.all_prod();
    cout << winner.last_win << endl;
    return 0;
}
