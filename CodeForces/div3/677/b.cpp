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
        int a[n];
        rep(i,n) cin >> a[i];
        int first_one = n-1;
        int last_one = 0;
        for(int i=0;i<n;i++){
            if(a[i]==1){
                first_one = i;
                break;
            }
        }
        for(int i=n-1;i>=0;i--){
            if(a[i]==1){
                last_one = i;
                break;
            }
        }

        if(first_one == last_one || (first_one== n-1 && last_one == 0)){
            cout << 0 << endl;
        }
        else{
            int ans = 0;
            for(int i=first_one;i<=last_one;i++){
                if(a[i]==0)ans++;
            }
            cout << ans << endl;
        }
    }
    return 0;
}