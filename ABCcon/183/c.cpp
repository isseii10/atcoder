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
    int n, k; cin >> n >> k;
    vector<vector<ll>> time(n, vector<ll>(n, 0));
    rep(i,n)rep(j,n) cin >> time[i][j];
    vector<int> town(n-1, 0);
    rep(i,n-1){
        town[i] = i+1;
    }

    int ans = 0;
    do{
        //rep(i,n-1) cout << town[i] << endl;
        int pre = 0;
        ll res = 0;
        rep(i,n-1){
            if(i==0){
                res += time[0][town[i]];
                pre = town[i];
            }
            else{
                res += time[pre][town[i]];
                pre = town[i];
            }
        }
        res += time[pre][0];
        if(res == k){
            ans++;
        }
    }while(next_permutation(town.begin(), town.end()));
    cout << ans << endl;
    return 0;
}