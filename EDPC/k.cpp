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

bool dp[100100];

int main() {
    int n, k; cin >> n >> k;
    int a[n];
    rep(i,n) cin >> a[i];
    dp[0] = false;
    for(int i=0;i<=k;i++){
        dp[i] = false;
        for(auto ai:a){
            if(i-ai>=0)
                dp[i] = dp[i] | !dp[i-ai];
        }
    }
    if(dp[k])cout << "First" << endl;
    else cout << "Second" << endl;
    return 0;
}