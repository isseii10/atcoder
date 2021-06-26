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
    ll k; cin >> k;
    ll n = 50;
    ll syo = k / n;
    ll amari = k%n;
    ll a[50];
    fill(a, a+50, n-1 + syo);
    ll count = amari;
    for(int i=0;i<n;i++){
        if (count > 0){
            a[i]++;
            count--;
            continue;
        }
        a[i] -= amari;
    }
    cout << n << endl;
    rep(i,n) {
        if (i!=n-1) cout << a[i] << " ";
        else cout << a[i] << endl;
    }
    return 0;
}