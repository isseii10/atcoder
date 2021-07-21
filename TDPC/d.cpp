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

ll devide(ll num, ll n){
    ll count = 0;
    while ( num % n == 0){
        num /= n;
        count++;
    }
    return count;
}

ll dp[101][65][65][65];

int main() {
    ll n, d;
    cin >> n >> d;

    ll count_2 = devide(d, 2);
    ll count_3 = devide(d, 3);
    ll count_5 = devide(d, 5);

    rep(i, n){
        rep(c2, 60){
            rep(c3, 60){
                rep(c5, 60){
                    ll tmp = dp[i][c2][c3][c5];
                    //1
                    dp[i+1][c2][c3][c5] += tmp;
                    //2
                    dp[i+1][c2+1][c3][c5] += tmp;
                    //3
                    dp[i+1][c2][c3+1][c5] += tmp;
                    //4
                    dp[i+1][c2+2][c3][c5] += tmp;
                    //5
                    dp[i+1][c2][c3][c5+1] += tmp;
                    //6
                    dp[i+1][c2+1][c3+1][c5] += tmp;
                }
            }
        }
    }
    ll s = 0;
    for(int c2=count_2;c2 < 61;c2++){
        for(int c3=count_3;c3 < 61;c3++){
            for(int c5=count_5;c5 < 61;c5++){
                s += dp[n][c2][c3][c5];
            }
        }
    }
    
    cout << s / pow(6, n) << endl;
    return 0;
}