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

ll f(ll n){
    string n_str = to_string(n);
    int n_size = n_str.size();
    ll res = 0;
    ll n_keta = 1;
    for(int i=n_size-1;i>=0;i--){
        ll digit = n_str[i] - '0';
        res += n_keta*digit;
        if(i!=0)
            n_keta = n_keta * n;
    }
    return res;   
}

int main() {
    ll a; cin >> a;
    for(ll i=10;i<=10000;i++){
        if(f(i) == a){
            cout << i << endl;
            return 0;
        };
    }
    cout << -1 << endl;
    return 0;
}