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
    int p[n];
    rep(i,n) cin >> p[i];
    int count = 0;
    for(int i=1;i<n-1;i++){
        if(p[i-1]<p[i] && p[i]<p[i+1])count++;
        if(p[i-1]>p[i] && p[i]>p[i+1])count++;
    }
    cout << count << endl;
    return 0;
}