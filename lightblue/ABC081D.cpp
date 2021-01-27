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
    int n;
    cin >> n;
    int a[n];
    rep(i,n) cin >> a[i];

    int a_max = -10000000;
    int a_min = 10000000;
    int a_max_idx = 0,a_min_idx = 0;
    rep(i,n){
        if(a[i]>a_max){
            a_max = a[i];
            a_max_idx = i;
        }
        if(a[i]<a_min){
            a_min = a[i];
            a_min_idx = i;
        }
    }
    vector<P> ans;
    if(abs(a_max) >= abs(a_min)){
        rep(i,n){
            if(i==a_max_idx)continue;
            a[i] += a_max;
            ans.emplace_back(a_max_idx+1, i+1);
        }
        //全部正
        rep(i, n-1){
            ans.emplace_back(i+1, i+2);
        }
        cout << ans.size() << endl;
        for(auto x: ans){
            cout << x.first << " " << x.second << endl;
        }
    }
    else{
        rep(i,n){
            if(i==a_min_idx)continue;
            a[i] += a_min;
            ans.emplace_back(a_min_idx+1, i+1);
        }
        //全部負
        for(int i = n-1;i>0;i--){
            ans.emplace_back(i+1, i);
        }
        cout << ans.size() << endl;
        for(auto x: ans){
            cout << x.first << " " << x.second << endl;
        }
    }
    return 0;
}