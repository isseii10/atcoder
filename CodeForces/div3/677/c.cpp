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
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<ll> a(n);
        rep(i,n) cin >> a[i];
        ll max_size = *max_element(a.begin(), a.end());
        int ans = -1;
        rep(i, n){
            if(a[i]==max_size){
                if(i==0){
                    if(a[i+1] < max_size){
                        ans = i+1;
                        break;
                    }
                }
                else if(i==n-1){
                    if(a[i-1] < max_size){
                        ans = i+1;
                        break;
                    }
                }
                else{
                    if(a[i-1] < max_size || a[i+1] < max_size){
                        ans = i+1;
                        break;
                    }
                }
            }
        }
        cout << ans << endl;
    }
    return 0;
}