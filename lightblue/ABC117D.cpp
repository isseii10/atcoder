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
    ll n, k;
    cin >> n >> k;
    ll a[n];
    rep(i, n)cin >> a[i];

    int bit_len_k = 0;

    ll bit_count[60];
    fill(bit_count, bit_count+60, 0);

    rep(i,n){
        for(int j=0;j<60;j++){
            if(a[i] & (1<<j)) bit_count[j]++;
        }
    }
    ll x = 0;
    for(int i=bit_len_k-1;i>=0;i--){
        if (n%2==0){
            if(bit_count[i] < n/2){
                ll res = 1;
                rep(j,i){
                     res *= 2;
                }
                if(x+res <= k)
                    x += res;
            }
        }
        else{
            if(bit_count[i] <= n/2){
                ll res = 1;
                rep(j,i){
                    res *= 2;
                }
                if(x+res <= k)
                    x += res;
            }
        }
    }
    //cout << x << endl;
    ll ans = 0;
    rep(i,n){
        ans += x^a[i];
    }
    cout << ans << endl;
    return 0;
}