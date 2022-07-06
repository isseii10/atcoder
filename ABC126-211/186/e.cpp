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

long long GCD(long long a, long long b){
    if(a==0)return b;
    return GCD(b % a, a);
}

/*
返り値はa,bのGCD
a*x + b*y = gcd(a, b)を満たす整数x, yが、変数x, yのアドレスに入る
*/
long long extGCD(long long a, long long b, long long &x, long long &y){
    if(a==0){
        x = 0;
        y = 1;
        return b;
    }
    long long d = extGCD(b%a, a, y, x);
    /*
    Xに入ってほしいのは、Y-b/a*X
    Yに入ってほしいのは、X
    いま、X=y,Y=xなので
    Y-b/a*Xは、x-b/a*yになる。
    */
    x = x - b/a * y;
    return d;
}
void solve(){
    ll n, s, k; cin >> n >> s >> k;
    /*
    kx ≡ -s (mod n)
    nとkが互いに素かどうかで場合分け
    */
    ll g = GCD(n, k);
    if(s % g != 0){
        cout << -1 << endl;
    }
    else{
        n /= g; s/= g; k/= g;
        ll x, y;
        extGCD(k, n, x, y);
        if(x>0) x -= n;
        x *= -s;
        x %= n;
        cout << x << endl;
    }
}

int main() {
    int t; cin >> t;
    while(t--){
        solve();
    }
    return 0;
}