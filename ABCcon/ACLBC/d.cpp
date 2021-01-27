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

int op(int x, int y)
{
    return max(x, y);
}

int e()
{
    return 0;
}

int main() {
    int n, k;
    cin >> n >> k;
    segtree<int, op, e> seg(300005);
    int ans = 0;
    rep(i, n){
        int a;
        cin >> a;
        int l = max(a-k, 0);
        int r = min(a+k+1, 300005);
        int longest;
        longest = seg.prod(l, r); //[l, r)から最大値を取ってくる
        seg.set(a, longest+1); // seg[a]を更新
        ans = max(ans, longest+1);
    };
    cout << ans << endl;
}
