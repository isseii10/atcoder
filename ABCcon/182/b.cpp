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

//約数列挙O(n**0.5)
vector<long long> enum_divisors(long long N) {
    vector<long long> res;
    for (long long i = 1; i * i <= N; ++i) {
        if (N % i == 0) {
            res.push_back(i);
            // 重複しないならば i の相方である N/i も push
            if (N/i != i) res.push_back(N/i);
        }
    }
    // 小さい順に並び替える
    sort(res.begin(), res.end());
    return res;
}

int main() {
    ll n; cin >> n;
    ll a[n];
    rep(i,n) cin >> a[i];
    sort(a, a+n);
    ll ans = 0;
    ll ans_gcd = 2;
    rep(i,n){
        vector<ll> div_i = enum_divisors(a[i]);
        for(auto d: div_i){
            if(d==1)continue;
            ll res = 0;
            for(int j=0;j<n;j++){
                if(a[j] % d == 0) res++;
            }
            if(res > ans){
                ans = res;
                ans_gcd = d;
            }
        }
    }
    cout << ans_gcd << endl;
    return 0;
}