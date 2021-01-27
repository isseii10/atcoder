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
    vector<P> ab;
    rep(i,n) {
        ll a, b;
        cin >> a >> b;
        ab.emplace_back(b, a);
    }
    sort(ab.begin(), ab.end());
    ll start = 0;
    ll yuuyo = 0;
    bool clear = true;
    rep(i, n){
        yuuyo += ab[i].first - start - ab[i].second;
        if(yuuyo < 0){
            clear = false;
            break;
        };
        start = ab[i].first;
    }
    if(clear) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}