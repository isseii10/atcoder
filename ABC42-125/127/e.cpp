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
const int MAX = 500000;
const int MOD = 1000000007;
const double pi = 3.141592653589;
typedef modint1000000007 mint;

long long fac[MAX], finv[MAX], inv[MAX];
// テーブルを作る前処理
void COMinit() {
    fac[0] = fac[1] = 1;
    finv[0] = finv[1] = 1;
    inv[1] = 1;
    for (int i = 2; i < MAX; i++){
        fac[i] = fac[i - 1] * i % MOD;
        inv[i] = MOD - inv[MOD%i] * (MOD / i) % MOD;
        finv[i] = finv[i - 1] * inv[i] % MOD;
    }
}
// 二項係数計算
long long COM(int n, int k){
    if (n < k) return 0;
    if (n < 0 || k < 0) return 0;
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD;
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    COMinit();

    //x_aとx_bの距離がiで、y_aとy_bの距離がjであるときの、
    //(x_a,y_a),(x_b,y_b)の選び方
    mint count;
    mint res=0;
    rep(i,m)rep(j,n){
        if(i!=0 && j!=0)
            count = (mint)(m-i) * (mint)(n-j) *2*(i+j);
        else
            count = (mint)(m-i) * (mint)(n-j) * (i+j);
        
        res += count;
    }
    
    mint ans = 0;
    ans = COM(n*m-2, k-2)*res;
    cout << ans.val() << endl;
    return 0;
}