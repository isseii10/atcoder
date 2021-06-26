#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n;
    cin >> n;
    vector<tuple<string, int, int>> sp;
    rep(i, n){
        string s;
        int p;
        cin >> s >> p;
        sp.emplace_back(s, (-1)*p, i+1);
    }
    sort(sp.begin(), sp.end());
    rep(i, n) cout << get<2>(sp[i]) << endl;
}