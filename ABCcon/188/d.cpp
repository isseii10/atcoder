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
    int n; cin >> n;
    ll prime_cost; cin >> prime_cost;
    vector<vector<ll>> abc(n, vector<ll>(3));
    rep(i,n){
        cin >> abc[i][0] >> abc[i][1] >> abc[i][2];
        abc[i][0]--;
    }
    /*
    cout << endl;
    rep(i,n){
        cout << abc[i][0] << ' ' << abc[i][1] << ' ' << abc[i][2] << endl;
    }
    */
    map<ll, ll> mp;
    rep(i,n){
       mp[abc[i][0]] += abc[i][2];
       mp[abc[i][1]] -= abc[i][2]; 
    }
    //c++のmapはキーで順序保存されている（平衡二分木）
    //各操作logn
    //キーエラーなし（Pythonのdefaultdictとorderddictの合わせみたいな）
    ll now_cost = 0;
    ll all_cost = 0;
    ll pre_date = -1;
    for(auto date_cost : mp){
        ll date = date_cost.first;
        ll cost = date_cost.second;
        if(pre_date!=-1)
            all_cost += min(prime_cost, now_cost) * (date-pre_date);
        now_cost += cost;
        pre_date = date;
    }
    cout << all_cost << endl;
}