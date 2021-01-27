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

ll dp[101][10];

int main() {
    int h, w, k;
    cin >> h >> w >> k;
    
    if(w==1){
        cout << 1 << endl;
        return 0;
    }

    //前処理でビット全探索しておく。
    ll amida[w];
    fill(amida, amida+w, 0);
    amida[0] = 1;
    for(int i=1;i<w;i++){
        for(int j=0;j<(1<<i);j++){
            bool flag = true;
            for(int bit=0;bit<j-1;bit++){
                if((j >> bit) & (j >> (bit+1))){
                    flag = false;
                    break;
                }
            }
            if(flag){
                amida[i]++;
                amida[i] %= MOD;
            }
        }
    }

    //w>1のとき
    vector<vector<ll>> from_to(w, vector<ll>(w, 0));
    for(int from=0;from<w;from++){
        for(int to=0;to<w;to++){
            if(abs(from-to)>1)continue;


            if(from == to){
                int left = max(0, from-1);
                int right = max(0, w-1-from-1);
                from_to[from][to] = amida[left]*amida[right] % MOD;
            }
            else{
                int left, right;
                left = max(0, min(from, to)-1);
                right = max(0, w-1 - max(from, to)-1);
                from_to[from][to] = amida[left]*amida[right] % MOD;
            }
        }
    }
    //dp
    dp[0][0] = 1;
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(j==0){
                dp[i+1][j] = (dp[i][j]*from_to[j][j]%MOD + dp[i][j+1]*from_to[j+1][j]%MOD)%MOD;
            }
            else if(j==w-1){
                dp[i+1][j] = (dp[i][j]*from_to[j][j]%MOD + dp[i][j-1]*from_to[j-1][j]%MOD)%MOD;
            }
            else{
                dp[i+1][j] = ((dp[i][j-1]*from_to[j-1][j]%MOD + dp[i][j]*from_to[j][j]%MOD)%MOD + dp[i][j+1]*from_to[j+1][j]%MOD)%MOD;
            }
        }
    }
    cout << dp[h][k-1]%MOD << endl;
    return 0;
}