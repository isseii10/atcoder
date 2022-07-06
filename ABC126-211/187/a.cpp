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
    int a, b; cin >> a >> b;
    int sa = 0, sb = 0;
    while (a!=0)
    {
        sa += a % 10;
        a /= 10;
    }
    while (b!=0)
    {
        sb += b % 10;
        b /= 10;
    }
    if(sa >= sb){
        cout << sa << endl;
    }
    else{
        cout << sb << endl;
    }
    
    return 0;
}