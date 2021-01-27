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
    int h, w;
    cin >> h >> w;
    vector<string> s(h);
    rep(i,h) cin >> s[i];
    //yoko
    int ans = 0;
    rep(i,h){
        rep(j,w-1){
            if(s[i][j] == '.' && s[i][j+1] == '.')ans++;
        }
    }
    rep(i,h-1){
        rep(j,w){
            if(s[i][j] == '.' && s[i+1][j] == '.')ans++;
        }
    }
    cout << ans << endl;
    return 0;
}