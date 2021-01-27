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
    ll a[n];
    rep(i,n) cin >> a[i];

    ll a0 = a[n-1];
    int count = 1;
    for(int i=n-2;i>=0;i--){
        if(count%2==1) a0 -= a[i];
        else a0 += a[i];
        count++;
    }
    vector<ll> ans;
    ans.push_back(abs(a0));
    ll tmp = abs(a0);
    for(int i=1;i<n;i++){
        ll xi = a[i-1] - tmp/2;
        ans.push_back(2*xi);
        tmp = 2*xi; 
    }
    rep(i,n)
        cout << ans[i] << " ";
    cout << endl;
    return 0;
}