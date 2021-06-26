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
    int a, b; cin >> a >> b;
    a--; b--;
    vector<vector<char>> white(50, vector<char> (100, '.'));
    vector<vector<char>> black(50, vector<char> (100, '#'));
    
    if(b != 0){
        bool black_flag = false;
        for(int i=0;i<50;i+=2){
            for(int j=0;j<100;j += 2){
                white[i][j] = '#';
                b--;
                if(b == 0){
                    black_flag = true;
                    break;
                }
            }
            if(black_flag)break;
        }
    }
    if(a != 0){
        bool white_flag = false;
        for(int i=1;i<50;i+=2){
            for(int j=0;j<100;j += 2){
                black[i][j] = '.';
                a--;
                if(a == 0){
                    white_flag = true;
                    break;
                }
            }
            if(white_flag)break;
        }
    }
    cout << 100 << ' ' << 100 << endl;
    rep(i,50){
        rep(j,100){
            if(j==99) cout << white[i][j] << endl;
            else cout << white[i][j];
        }
    }
    rep(i,50){
        rep(j,100){
            if(j==99) cout << black[i][j] << endl;
            else cout << black[i][j];
        }
    }
}