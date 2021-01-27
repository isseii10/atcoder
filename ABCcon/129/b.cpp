#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n;
    cin >> n;
    int w[n];
    int ans = 1000000000;
    rep(i, n)cin >> w[i];
    rep(t, n-1){
        int s1 = 0;
        int s2 = 0;
        for (int i = 0;i <= t;i++)s1 += w[i];
        for (int j = t+1;j<n;j++)s2 += w[j];
        ans = min(ans, abs(s1-s2));
    }
    cout << ans << endl;
}