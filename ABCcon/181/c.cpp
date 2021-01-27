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
    int x[n], y[n];
    rep(i,n) cin >> x[i] >> y[i];
    bool yes_flag = false;
    for(int i=0;i<n-1;i++){
        for(int j=i+1;j<n;j++){
            for(int k=0;k<n;k++){
                if(k==i || k==j)continue;
                if((x[j]-x[i])*y[k] == (y[j]-y[i])*x[k] + y[i]*(x[j]-x[i]) - (y[j]-y[i])*x[i]){
                    yes_flag = true;
                    break;
                }

            }
            if(yes_flag)break;
        }
        if(yes_flag)break;
    }
    if(yes_flag)cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}