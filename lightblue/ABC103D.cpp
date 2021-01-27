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
    int n, m;
    cin >> n >> m;
    vector<P> ba(m);
    rep(i,m){
        cin >> ba[i].second >> ba[i].first;
        ba[i].first--;
        ba[i].second--;
    }
    sort(ba.begin(), ba.end());

    int ans = 0;
    int end = 0;
    rep(i,m){
        int b = ba[i].first;
        int a = ba[i].second;
        if(a>=end){
            end = b;
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}