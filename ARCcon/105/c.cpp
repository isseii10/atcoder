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
    int n, m;
    cin >> n >> m;

    vector<int> w(n);
    rep(i,n)cin >> w[i];
    sort(w.begin(), w.end());

    vector<P> vl(m);
    rep(i,m) cin >> vl[i].second >> vl[i].first;
    sort(vl.begin(),vl.end());
    rep(i,m-1){
        vl[i+1].second = max(vl[i+1].second, vl[i].second); //lでマックスとっていく
    }
    vector<int> v(m);
    rep(i,m) v[i] = vl[i].first;

    int w_max = *max_element(w.begin(), w.end());
    int v_min = *min_element(v.begin(), v.end());
    if(w_max>v_min){
        cout << -1 << endl;
        return 0;
    }

    //順列全探索
    ll ans = LINF;
    do{
        vector<int> sum_w(n+1, 0);
        rep(i, n) sum_w[i+1] = sum_w[i] + w[i];

        //ここから有向グラフ化
        //i→j間は、i~jのラクダたちが含まれるので重さの総和でにぶたんして辺の長さを決める
        vector<vector<P>> edge(n, vector<P>(0));
        //i,jは1-indexed
        for(int i=1;i<n;i++){
            for(int j=i+1;j<=n;j++){
                int weight = sum_w[j]-sum_w[i-1];
                auto itr = lower_bound(vl.begin(), vl.end(), make_pair(weight, 0));
                if(itr==vl.begin())
                    edge[i-1].emplace_back(j-1, 0); //edgeは0-indexed
                else
                    edge[i-1].emplace_back(j-1,vl[itr-vl.begin()-1].second);
            }
        }
        //bfsで距離調べる
        queue<int> q;
        q.push(0);
        vector<int> dist(n, -1);
        dist[0] = 0;
        while(!q.empty()){
            int p = q.front();
            q.pop();
            for(auto c :edge[p]){
                if(dist[c.first]!=-1){
                    dist[c.first] = max(dist[c.first], dist[p] + c.second);
                    continue;
                }
                q.push(c.first);
                dist[c.first] = dist[p] + c.second;
            }
        }
        ll res = dist[n-1];
        ans = min(ans, res);
    }while(next_permutation(w.begin(), w.end()));
    cout << ans << endl;
    return 0;
}