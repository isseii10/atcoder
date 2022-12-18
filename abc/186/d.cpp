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
    rep(i,n)cin >> a[i];
    sort(a.begin(), a.end());
    vector<ll> sum_a(n);
    sum_a[0] = a[0];
    for(int i=1;i<n;i++){
        sum_a[i] = sum_a[i-1] + a[i];
    }
    ll ans = 0;
    rep(i,n){
        ll now = a[i];
        ll now_ijou = sum_a[n-1] - sum_a[i];
        ll sa = (n-1 - i)*now;
        ans += now_ijou - sa;
    }
    cout << ans << endl;

    /*
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            ans += abs(a[i] - a[j]); 
        }
    }
    */
    return 0;
}