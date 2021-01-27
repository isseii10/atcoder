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
    int n, m; cin >> n >> m;
    vector<int> a(m);
    rep(i,m) cin >> a[i];
    a.push_back(0);
    a.push_back(n+1);
    sort(a.begin(), a.end());
    int aida = n+10;
    rep(i,m+1){
        if(a[i+1]-a[i]-1 <= 0)continue;
        aida = min(aida, a[i+1]-a[i]-1);
    }
    int ans = 0;
    rep(i,m+1){
        if(a[i+1]-a[i]-1 <= 0)continue;
        if((a[i+1]-a[i]-1)%aida == 0){
            ans += (a[i+1]-a[i]-1)/aida;
        }
        else{
            ans += (a[i+1]-a[i]-1)/aida + 1;
        }
    }
    cout << ans << endl;
    return 0;
}