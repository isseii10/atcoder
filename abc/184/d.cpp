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

double dp[110][110][110];

int main() {
    int a, b, c; cin >> a >> b >> c;
    dp[a][b][c] = 1;
    for(int i=a;i<=100;i++){
        for(int j=b;j<=100;j++){
            for(int k=c;k<=100;k++){
                if(i==100 || j == 100 || k == 100){
                    continue;
                }
                dp[i+1][j][k] += dp[i][j][k] * i/(i+j+k);
                dp[i][j+1][k] += dp[i][j][k] * j/(j+i+k);
                dp[i][j][k+1] += dp[i][j][k] * k/(k+i+j);
            }
        }
    }
    double ans = 0;
    for(int j=b;j<100;j++){
        for(int k=c;k<100;k++){
            int count = 100-a + j-b + k-c;
            ans += dp[100][j][k] * count;
        }
    }
    for(int i=a;i<100;i++){
        for(int k=c;k<100;k++){
            int count = i-a + 100-b + k-c;
            ans += dp[i][100][k] * count;
        }
    }
    for(int i=a;i<100;i++){
        for(int j=b;j<100;j++){
            int count = i-a + j-b + 100-c;
            ans += dp[i][j][100] * count;
        }
    }
    cout << setprecision(15) << ans << endl;
    return 0;
}