
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
    string a, b, c;
    cin >> a >> b >> c;
    bool siritoriFlag = false;
    if (a[a.size()-1] == b[0] && b[b.size()-1] == c[0]) siritoriFlag = true;

    if(siritoriFlag)cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}