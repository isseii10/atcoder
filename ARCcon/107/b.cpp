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
    ll n, k; cin >> n >> k;
    ll ans = 0;
    if(k<0) k = -k;
    for(int i=2;i<=2*n;i++){
        if(i-k<2)continue;
        if(i-1>n){
            if(i-k-1>n){
                ans += (2*n-i+1)*(2*n-(i-k)+1);
            }
            else{
                ans += (2*n-i+1)*(i-k-1);
            }
        }
        else{
            if(i-k-1>n){
                ans += (i-1)*(2*n-(i-k)+1);
            }
            else{
                ans += (i-1)*(i-k-1);
            }
        }
    }
    cout << ans << endl;
    return 0;
}