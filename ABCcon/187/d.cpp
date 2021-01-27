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
    //int型で全部計算して、オーバーフローにきづけなかった
    //intは2*10**9程度までしか表せないので、
    //a,bの制約が10**9では、2*a + bでオーバーフローする可能性があった

    //全部ll使え！！！

    int n; cin >> n;
    ll a[n], b[n];
    ll sort_a[n], sort_b[n];
    rep(i,n){
        cin >> a[i] >> b[i];
    }
    vector<pair<ll, ll>> sum_ab(n);
    ll aoki = 0;
    rep(i,n){
        sum_ab[i].first = 2*a[i] + b[i];
        sum_ab[i].second = i;
        aoki += a[i];
    }
    sort(sum_ab.rbegin(), sum_ab.rend());
    rep(i,n){
        sort_a[i] = a[sum_ab[i].second];
        sort_b[i] = b[sum_ab[i].second];
    }
    ll takahashi = 0;
    rep(i,n){
        if(takahashi > aoki){
            cout << i << endl;
            return 0;
        }
        takahashi += sort_a[i] + sort_b[i];
        aoki -= sort_a[i];
    }
    cout << n << endl;
    return 0;
}