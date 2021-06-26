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

map<ll, ll> mp;

int main() {
    int n;
    cin >> n;
    int ans = 0;
    rep(i,n){
        ll a;
        cin >> a;
        mp[a]++;
        if(mp[a] != 0){
            if(mp[a]%2==0) ans--;
            else ans++;
        }
    }
    cout << ans << endl;
    return 0;
}