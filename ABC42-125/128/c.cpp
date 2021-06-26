#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n, m;
    cin >> n >> m;
    vector<vector<int>> lump(m);
    rep(i, m){
        int k;
        cin >> k;   
        rep(j, k){
            int s;
            cin >> s;
            lump[i].push_back(s-1);
        };
    };
    int p[m];
    rep(i, m) cin >> p[i];

    //bit全探索
    int ans = 0;
    for (int bit = 0; bit < (1<<n); bit++){ //各スイッチのon,offの状態を全通り
        vector<int> count(m, 0); //各電球につながっているスイッチがオンになっている個数を記録
        rep(i, n){
            if((bit>>i) & 1){ //スイッチiがオンならば
                rep(j, m){ //電球jについて
                    for (auto x: lump[j]){ //電球jにつながっているスイッチxについて
                        if (x == i)count[j] += 1;
                    }
                }
            }
        }
        int on = 0;
        rep(i, m)
            if(count[i]%2 == p[i])on += 1;
        if(on == m)ans += 1;
    }
    cout << ans << endl;

}