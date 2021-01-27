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
    int n;
    ll a, b;
    cin >> n >> a >> b;
    ll c = a-b;
    ll h[n];
    rep(i,n) cin >> h[i];
    ll left = 0;
    ll right = 10000000000;
    while (right - left > 1){
        ll mid = (right + left)/2;
        vector<ll> still;
        rep(i,n){
            if(h[i] <= mid*b)continue;
            still.push_back(h[i]-mid*b);
        }
        ll count = mid;
        for(auto x : still){
            count -= x / c + 1;
            if(x % c == 0) count++;
        }
        if(count < 0) left = mid;
        else right = mid;
    }
    cout << right << endl;
    return 0;
}