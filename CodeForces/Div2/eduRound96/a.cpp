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
    while (t--)
    {
        int n; cin >> n;
        bool find = false;
        rep(i,n/3+1){
            rep(j,n/5+1){
                if((n-i*3-j*5)>=0 && (n-i*3-j*5)%7==0){
                    cout << i << " " << j << " " << (n-i*3-j*5)/7 << endl;
                    find = true;
                    break;
                }
            }
            if(find)break;
        }
        if(!find)
            cout << -1 << endl;
    }
    
    return 0;
}