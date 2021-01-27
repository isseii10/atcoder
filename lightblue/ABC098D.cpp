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
    ll sxor[n+1], sa[n+1];
    sa[0] = 0;
    sxor[0] = 0;
    rep(i,n){
        sa[i+1] = sa[i] + a[i];
        sxor[i+1] = sxor[i] ^ a[i];
    }
    //尺取り法
    
    ll ans = 0;
    int r = 1;
    for(int l=1;l<=n;l++){
        while(r <=n && sa[r]-sa[l-1] == (sxor[r]^sxor[l-1])){
            r++;
        }
        ans += r-l;

        if(l==r)r++;
    }
    /*にぶたん
    ll ans = 0;
    for(int i=1;i<=n;i++){
        int left = i;
        int right = n+1;
        while(right-left>1){
            int mid = (left+right)/2;
            if((sa[mid]-sa[i-1]) == (sxor[mid]^sxor[i-1]))
                left = mid;
            else
                right = mid;
        }
        ans += left - i+1;
    }
    */

    cout << ans << endl;
    return 0;

}