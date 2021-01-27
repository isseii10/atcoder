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
    int a, b, c, x;
    cin >> a >> b >> c >> x;
    int ans = 0;
    rep(i,a+1){
        rep(j,b+1){
            rep(k,c+1){
                if(500*i+100*j+50*k==x)ans += 1;
            }
        }
    }
    cout << ans << endl;
    return 0;
}