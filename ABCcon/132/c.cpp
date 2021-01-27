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
    int d[n];
    rep(i,n) cin >> d[i];
    sort(d, d+n);
    int count = 0;
    for(int k=1;k<100001;k++){
        auto itr = lower_bound(d, d+n, k);
        if(itr-d == d+n-itr)
            count++; 
    } 
    cout << count << endl;
    return 0;
}