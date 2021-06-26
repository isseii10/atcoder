#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
using namespace atcoder;
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
    int n, m;
    cin >> n >> m;
    dsu d(n);
    rep(i, m){
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        d.merge(a, b);
    };
    set<int> renketu;
    rep(i, n){
        renketu.insert(d.leader(i));
    };
    long unsigned int ans = 0;
    ans = renketu.size() - 1;
    cout << ans << endl;
}