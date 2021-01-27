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


//BIT 1-indexed
class BIT{
public:
    ll n;
    vector<ll> bit;
    BIT(ll _n) : n(_n), bit(_n+1, 0){}

    //bit_iにxを加算
    void add_value(ll i, ll x){
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k & -k)){
            bit[k] += x;
        }
    }

    void set_value(ll i, ll x){
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k&-k)){
            bit[k] = max(bit[k], x);
        }
    }

    ll sum_value(ll i){
        ll s = 0;
        if(i==0) return s;
        for(ll k=i;k>0;k-=(k&-k)){
            s += bit[k];
        }
        return s;
    }

    ll max_value(ll i){
        ll m = 0;
        if(i==0) return m;
        for(ll k=i;k>0;k-=(k&-k)){
            m = max(m, bit[k]);
        }
        return m;
    }

};

ll dp[210000];

int main(){
    int n; cin >> n;
    int h[n];
    BIT bit(n);
    vector<P> flowers(n);
    rep(i,n) {
        cin >> h[i];
        flowers[i] = make_pair(h[i], i);
    }
    sort(flowers.begin(), flowers.end());
    int a[n];
    rep(i,n){
        cin >> a[i];
    }
    
    for(auto p : flowers){
        int i = p.second;
        dp[i] = bit.max_value(i) + a[i];
        bit.set_value(i+1, dp[i]);
    }
    cout << bit.max_value(n) << endl;
    return 0;
}