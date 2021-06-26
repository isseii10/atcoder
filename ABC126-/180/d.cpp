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
    ll x, y, a, b;
    cin >> x >> y >> a >> b;

    ll xp = 0;
    while(true){
        if(y/a < x)break; // a*xがオバーフローする危険性があるので
        if(y <= a*x)break;
        if(a*x > x+b)break;
        xp++;
        x *= a;        
    }

    xp += (y-x-1)/b;
    cout << xp << endl;
    return 0;
}