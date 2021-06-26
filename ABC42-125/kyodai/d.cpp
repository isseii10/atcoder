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
    int n; cin >> n;
    int len[n];
    rep(i, n) {
        len[i] = 2*(i+1)-1;
    }
    if(n%2==0){
        if(n == 2){
            cout << "impossible" << endl;
            return 0;
        }
        cout << n/2 << endl;
        rep(i, n/2){
            cout << 2 << " " << len[i] << " " << len[n-1-i] << endl;
        }
    }
    else{

    }

    return 0;
}