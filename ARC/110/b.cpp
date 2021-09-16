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
    int n; cin >> n;
    string t; cin >> t;
    string s_unit = "110";
    ll loop = n/3;
    rep(i,loop)s_unit += "110";
    loop++;
    vector<int> sa1 = suffix_array(s_unit);
    ll ans1 = 0;
    vector<int> lcp1 = lcp_array(t, sa1);
    for(auto x : lcp1){
        if(x == n-1) ans1++;
    }
    s_unit += s_unit;
    vector<int> sa2 = suffix_array(s_unit);
    ll ans2 = 0;
    vector<int> lcp2 = lcp_array(t, sa2);
    for(auto x : lcp2){
        if(x == n-1)ans2++;
    }
    ans2 -= 2*ans1;
    cout << ans1 << endl;
    cout << ans2 << endl;
    ll total_ans = 0;
    total_ans = ans1*(10000000000 / loop) + ans2*(10000000000 / 2*loop);
    cout << total_ans << endl;
    return 0;
}