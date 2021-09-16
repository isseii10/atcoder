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

//素因数分解O(n**0.5)
vector<pair<long long, long long> > prime_factorize(long long N) {
    vector<pair<long long, long long> > res;
    for (long long a = 2; a * a <= N; ++a) {
        if (N % a != 0) continue;
        long long ex = 0; // 指数
        // 割れる限り割り続ける
        while (N % a == 0) {
            ++ex;
            N /= a;
        }
        // その結果を push
        res.push_back({a, ex});
    }
    // 最後に残った数について
    if (N != 1) res.push_back({N, 1});
    return res;
}


int main() {
    ll n; cin >> n;
    int A = 0;
    int B = 0;
    ll res = 1;
    bool out_flag = false;
    while(true){
        vector<pair<ll, ll>> prime;
        prime = prime_factorize(n-res);
        for(auto p: prime){
            cout << p.first <<" " << p.second << endl;
        }

        if((prime.size()==1) && (prime[0].first!=3)){
            A = prime[0].second;
            break;
        }
        if(res*5>=n){
            out_flag = true;
            break;
        }
        else {
            res*=5;
            B++;
        }
    }
    if(out_flag) cout << -1 << endl;
    else cout << A << " " << B << endl;
    return 0;
}