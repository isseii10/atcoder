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
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        
        ll sax = abs(x2-x1);
        ll say = abs(y2-y1);
        if(sax!=0 && say != 0)
            cout << sax + say + 2 << endl;
        else cout << sax + say << endl;
    }
    return 0;
}