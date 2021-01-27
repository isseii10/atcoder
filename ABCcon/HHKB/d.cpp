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
typedef modint1000000007 mint;

int main() {
    int t; cin >> t;
    rep(t_,t){
        ll n, a, b;
        cin >> n >> a >> b;
        if(a+b>n){
            cout << 0 << endl;
            continue;
        }
        mint all_count = (mint)(n-a+1)*(mint)(n-a+1)*(mint)(n-b+1)*(mint)(n-b+1);
        //重なっているのを引く
        mint kasanari = (mint)(n-a+1)*(mint)(n-b+1) - (mint)(n-a-b+2)*(mint)(n-a-b+1);
        mint ans = all_count - (kasanari*kasanari);
        cout << ans.val() << endl; 


    }
    return 0;
}