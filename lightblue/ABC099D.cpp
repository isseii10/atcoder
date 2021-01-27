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
    int d[C][C];
    rep(i,C)rep(j,C) cin >> d[i][j];
    int c[n][n];
    rep(i,n)rep(j,n) cin >> c[i][j];

    vector<map<int,int>> color(3);
    rep(i,3){
        rep(j,n){
            rep(k,n){
                if(i == (j+1+k+1)%3){
                    color[i][c[j][k]] += 1;
                }
            }
        }
    }
    


    return 0;
}