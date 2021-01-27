#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int p, q, r;
    cin >> p >> q >> r;
    int ans = 1000;
    ans = min(p+q, ans);
    ans = min(ans, q + r);
    ans = min(ans, r + p);
    cout << ans << endl;
}