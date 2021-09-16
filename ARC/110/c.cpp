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
    int n; cin >> n;
    int p[n];
    rep(i,n) cin >> p[i];
    vector<P> move(n);
    int left = 0;
    int right  = 0;
    rep(i, n){
        int res = p[i] - i+1;
        if(res<0){
            left += abs(res);
            move[i].first = -1;
            move[i].second = abs(res);
        }
        else{
            right += res;
        }
    }
    if(left != right){
        cout << -1 << endl;
        return 0;
    }



    return 0;
}