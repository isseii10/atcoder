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
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    if(r1==r2 && c1==c2){
        cout << 0 << endl;
        return 0;
    }
    if(r1 + c1 == r2 + c2 || r1 - c1 == r2 - c2){
        cout << 1 << endl;
        return 0;
    }
    else if(abs(r1-r2) + abs(c1-c2) <= 3){
        cout << 1 << endl;
        return 0;
    }
    else if(c2 >= r2 - r1 + c1 - 4 && c2 <= r2 - r1 + c1 + 4){
        cout << 2 << endl;
        return 0;
    }
    else if(c2 >= -r2 +r1 + c1 - 4 && c2 <= -r2 + r1 + c1 + 4){
        cout << 2 << endl;
        return 0;
    }
    else if(abs(c1 - r1) % 2 == abs(c2 - r2) % 2){
        cout << 2 << endl;
        return 0;
    }
    else{
        cout << 3 << endl;
        return 0;
    }
    return 0;
}