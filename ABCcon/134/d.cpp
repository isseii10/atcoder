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
    int n; cin >> n;
    int a[n+1];
    rep(i,n) cin >> a[i+1];
    vector<vector<ll>> divs(n+1);
    for(int i=1; i<=n;i++){
        divs[i] = enum_divisors(i);
    }

    vector<int> ans(n+1, 0);
    vector<int> b;
    for(int i=n;i>=1;i--){
        if(a[i]==ans[i]%2)continue;
        b.push_back(i);
        for(auto div : divs[i])
            ans[div]++;
    }

    for(int i=1;i<=n;i++){
        ans[i] %= 2;
    }
    
    int m=b.size();
    cout << m << endl;
    for(auto bi: b){
        cout << bi << " ";
    }
    cout <<endl;

    return 0;
}