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
    vector<ll> a(n);
    rep(i,n) cin >> a[i];
    vector<ll> sa(n);
    sa[0] = a[0];
    for(int i=1;i<n;i++){
        sa[i] = sa[i-1] + a[i];
    }
    vector<ll> move_end_pos(n);
    move_end_pos[0] = a[0];
    for(int i=1;i<n;i++){
        move_end_pos[i] = move_end_pos[i-1] + sa[i];
    }
    vector<ll> until_move_max(n);
    ll here = a[0];
    until_move_max[0] = a[0];
    for(int i=1;i<n;i++){
        until_move_max[i] = max(until_move_max[i-1], here + a[i]);
        here += a[i];
    }
    /*
    rep(i,n){
        cout << until_move_max[i] << endl;
    }
    */
   ll now = 0;
   ll ans = 0;
    rep(i,n){
        ll res = now + until_move_max[i];
        ans = max(ans, res);
        now = move_end_pos[i];
    }
    cout << ans << endl;
    return 0;
}