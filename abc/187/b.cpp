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
    vector<P> iti(n);
    rep(i,n){
        cin >> iti[i].first >> iti[i].second; 
    }
    int ans = 0;
    rep(i,n-1){
        for(int j=i+1;j<n;j++){
            int x1 = iti[i].first;
            int x2 = iti[j].first;
            int y1 = iti[i].second;
            int y2 = iti[j].second;
            if(x2-x1 < 0){
                if(((y2-y1) <= (x1-x2)) && ((y2-y1) >= (x2-x1))){
                    ans++;
                }
            }
            else{
                if(((y2-y1) >= (x1-x2)) && ((y2-y1) <= (x2-x1))){
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;
    return 0;
}