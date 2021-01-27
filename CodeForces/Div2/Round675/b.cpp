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
    int t;
    cin >> t;
    rep(p,t){
        ll n, m; cin >> n >> m;
        ll a[n][m];
        rep(i,n)rep(j,m) cin >> a[i][j];
        ll ans = 0;
        rep(i,n){
            bool rflag = false;
            if(n%2 == 1){
                if(i>n/2)continue;
                if(i==n/2)rflag = true;
            }
            else {
                if(i > n/2-1)continue;
            }
            rep(j,m){
                bool cflag = false;
                if(m%2 == 1){
                    if(j>m/2)continue;
                    if(j==m/2)cflag = true;
                }
                else {
                    if(j > m/2-1)continue;
                }
                //a[i][j],a[n-1-i][j],a[i][m-1-j],a[n-1-i][m-1-j]
                if(cflag && rflag)continue;
                else if(cflag && !rflag){
                    ans += abs(a[i][j]-a[n-i-1][j]);
                }
                else if(!cflag && rflag){
                    ans += abs(a[i][j]-a[i][m-j-1]);
                }
                else{
                    ll abcd[4] ={a[i][j], a[i][m-j-1], a[n-i-1][j], a[n-i-1][m-j-1]};
                    sort(abcd, abcd+4);
                    ll av = abcd[1];
                    ans += abs(a[i][j]-av);
                    ans += abs(a[i][m-j-1]-av);
                    ans += abs(a[n-i-1][j]-av);
                    ans += abs(a[n-i-1][m-j-1]-av);

                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}