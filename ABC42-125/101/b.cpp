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
    int n;
    cin >> n;
    int s = 0;
    int n_ = n;
    while(n_!=0){
        s += n_ % 10;
        n_ /= 10;
    }
    if (n % s == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}