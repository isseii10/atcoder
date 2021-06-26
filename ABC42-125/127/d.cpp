#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> a(n);
    map<int, int, greater<int>> dict;
    rep(i, n){
        cin >> a[i];
        dict[a[i]] += 1;
    }
    rep(i, m){
        int b, c;
        cin >> b >> c;
        dict[c] += b;
    }
    ll ans = 0;
    ll count = n;
    for(auto x : dict){
        ll key = x.first;
        ll value = x.second;
        if (count < value) value = count;
        ans += key*value;
        count -= value;
        if (count == 0)break;
    };
    cout << ans << endl;
}