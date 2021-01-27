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
    int n, k;
    cin >> n >> k;
    int a[n];
    rep(i,n) cin >> a[i];
    int count = 0;
    if(k >= n) cout << 1 << endl;
    else{
        n -= k;
        count++;
        count += n / (k-1);
        if(n % (k-1) != 0)count++;
        cout << count << endl;
    }
    return 0;
}