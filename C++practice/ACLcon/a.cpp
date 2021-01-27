#include <bits/stdc++.h>
#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
using namespace atcoder;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> P;

int main() {
    int n;
    cin >> n;
    int xy[n][2];
    rep(i, n) cin >> xy[i][0] >> xy[i][1];
    dsu d(n);
}