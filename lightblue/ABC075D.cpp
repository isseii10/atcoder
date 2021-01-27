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
    int n, k;
    cin >> n >> k;
    vector<pair<ll, ll>> xy(n);
    rep(i,n) cin >> xy[i].first >> xy[i].second;
    sort(xy.begin(), xy.end());
    ll ans = 9220000000000000000;
    for(int l=0; l<n-1; l++){
        ll left = xy[l].first;
        for(int r=l+1; r<n;r++){
            ll right = xy[r].first;
            ll x = abs(left - right);
            for(int d=0;d<n-1;d++){
                ll down = xy[d].second;
                for(int u=d+1;u<n;u++){
                    ll up = xy[u].second;
                    ll y = abs(down-up);
                    int count = 0;
                    rep(i,n){
                        if(left<=xy[i].first && xy[i].first<=right){
                            if(min(down,up)<=xy[i].second && xy[i].second<=max(down,up)){
                                count++;
                            }
                        }
                    }
                    if(count>=k) ans = min(ans, x*y);
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}