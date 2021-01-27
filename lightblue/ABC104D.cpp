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
    int d, g;
    cin >> d >> g;
    vector<P> pc(d);
    rep(i,d) cin >> pc[i].first >> pc[i].second;

    int ans = 1000000;
    for(int i=0;i < (1<<d);i++){
        int score = 0;
        int res = 0;
        for(int j=0;j<d;j++){
            if(i >> j & 1){
                score += 100*(j+1)*pc[j].first;
                score += pc[j].second;
                res += pc[j].first;
            }
        }
            
        if(score < g){
            for(int k=d-1;k>=0;k--){
                if((i>>k&1) == 0){
                    int count = 0;
                    while(count < pc[k].first && score<g){
                        score += 100*(k+1);
                        res += 1;
                        count += 1;
                    }
                    if(score>=g)break;
                }
            }
        }
        ans = min(ans, res);
    }
    cout << ans << endl;
    return 0;
}