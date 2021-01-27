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
    int t; cin >> t;
    while(t--){
        string x; cin >> x;
        int count = 0;
        int x_int = stoi(x);
        int x_0 = x_int % 10;
        int n = x.size();
        count += (x_0-1)*10;
        count += n*(n+1)/2;
        cout << count << endl;
    }
    return 0;
}