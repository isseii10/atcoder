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
    int n, C;
    cin >> n >> C;
    vector<vector<P>> tm(C, vector<P>(0));
    vector<int> time(100100, 0);
    rep(i,n){
        int s, t, c;
        cin >> s >> t >> c;
        c--;
        tm[c].emplace_back(s,t);
    }
    rep(i, C){
        
        sort(tm[i].begin(), tm[i].end());
        if(tm[i].size()>1){
            for(ull j=0;j<tm[i].size()-1;j++){
                if (tm[i][j].second == tm[i][j+1].first)
                    tm[i][j].second -= 1;
            }
        }
    }

    rep(i,C){
        ull sz = tm[i].size();
        for(ull j=0;j<sz;j++){
            time[tm[i][j].first] += 1;
            time[tm[i][j].second +1] -= 1; 
        }
    }
    for(int i=1;i<100002;i++) time[i] += time[i-1];

    int ans = 0;
    rep(i,100002) ans = max(ans, time[i]);
    cout << ans << endl;
    return 0;
}