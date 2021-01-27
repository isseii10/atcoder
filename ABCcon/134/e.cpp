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
    vector<int> a(n);
    rep(i,n) cin >> a[i];
    deque<int> d;
    rep(i,n){
        auto idx = lower_bound(d.begin(), d.end(), a[i])-d.begin();
        if(idx==0)
            d.push_front(a[i]);
        else
            d[idx-1] = a[i];
    }
    cout << (int)d.size() << endl;

    return 0;
}