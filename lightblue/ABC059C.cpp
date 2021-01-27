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
    ll s[n];
    ll ans = LINF;
    rep(i,2){
        ll res = 0;
        //最初正
        if (i==0){
            if (a[0] <= 0){
                s[0] = 1;
                res += 1-a[0];
            }
            else s[0] = a[0];
        }
        //最初負
        else{
            if(a[0]>=0){
                s[0] = -1;
                res += a[0]+1;
            }
            else s[0] = a[0];
        }
        for(int j = 1;j<n;j++){
            s[j] = a[j] + s[j-1];
            if(s[j-1]<0 && s[j]<=0){
                res += 1-s[j];
                s[j] = 1;
            }
            else if(s[j-1]>0 && s[j]>=0){
                res += s[j]+1;
                s[j] = -1;
            }
        }
        ans = min(res, ans);
    }
    cout << ans << endl;
}