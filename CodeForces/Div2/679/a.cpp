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

int lcm(int x, int y){
    return x*y/gcd(x, y);
}

int main() {
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        int a[n];
        rep(i,n) cin >> a[i];
        int b[n];
        for(int i = 0; i<n-1;i+=2){
            int x = lcm(abs(a[i]), abs(a[i+1]));
            b[i] = -x/a[i];
            b[i+1] = x/a[i+1];
        }
        rep(i,n){
            cout << b[i] << " ";
        }
        cout << endl;
    }
    return 0;
}