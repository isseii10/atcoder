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
    int n, m, t;
    cin >> n >> m >> t;
    int a[m], b[m];
    rep(i,m) cin >> a[i] >> b[i];
    int now = n;
    rep(i,m){
        if(i==0){
            if(now <= a[i]){
                cout << "No" << endl;
                return 0;
            }
            now -= a[i];
            now += b[i]-a[i];
            now = min(now, n);
        }
        else{
            if(now <= a[i] - b[i-1]){
                cout << "No" << endl;
                return 0;
            }
            now -= a[i] - b[i-1];
            now += b[i] - a[i];
            now = min(now, n);
        }
    }
    if(now <= t - b[m-1]){
        cout << "No" << endl;
        return 0;
    }
    cout << "Yes" << endl;
    return 0;
}