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
    sort(res.rbegin(), res.rend());
    return res;
}

int main() {
    int n, k;
    cin >> n >> k;
    ll a[n];
    ll sum_a = 0;
    rep(i,n) {
        cin >> a[i];
        sum_a += a[i];
    }
    
    vector<ll> aim = enum_divisors(sum_a);
    ll ans = 0;
    bool found = false;
    for(auto x : aim){
        vector<ll> b(n, 0);
        vector<ll> sum_b(n, 0);
        for(int i=0;i<n;i++){
            b[i] = a[i]%x;
        }
        sort(b.begin(), b.end());
        sum_b[0] = b[0];
        for(int i=0;i<n-1;i++){
            sum_b[i+1] = sum_b[i] + b[i+1];
        }
        for(int i=0;i<n;i++){
            if(sum_b[i] == x*(n-i-1)-(sum_b[n-1]-sum_b[i])){
                if(sum_b[i]<= k){
                    ans = x;
                    found = true;
                    break;
                }
            }
        }
        if(found)break;
    }
    cout << ans << endl;

    return 0;
}