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
    char s, t;
    cin >> s >> t;
    char ans;
    if(s=='Y'){
        if(t=='a')ans = 'A';
        else if(t=='b')ans = 'B';
        else ans = 'C';
    }
    else{
        ans = t;
    }
    cout << ans << endl;
    return 0;
}