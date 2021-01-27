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
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int abcd[4] = {a, b, c, d};
    for(int i=0;i<(1<<4);i++){
        ll eat = 0;
        ll no_eat = 0;
        for(int j=0;j<4;j++){
            if((i>>j)&1){
                eat += abcd[j];
            }
            else{
                no_eat += abcd[j];
            }
        }
        if(eat == no_eat){
            cout << "Yes" << endl;
            return 0;
        }
    }
    cout << "No" << endl;
    return 0;
}