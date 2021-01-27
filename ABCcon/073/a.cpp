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
    string n; cin >> n;
    bool nine_flag = false;
    for (auto c : n){
        if(c=='9'){
            nine_flag = true;
        }
    }
    if(nine_flag) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}