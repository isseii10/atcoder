#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
//using namespace atcoder;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> P;

int main() {
    double W, H, x, y;
    cin >> W >> H >> x >> y;
    double ans = W*H*0.5;
    int c = 0;
    if (x == W/2 && y == H/2) c = 1;
    cout << ans << " " << c << endl;
}