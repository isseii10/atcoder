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
    int a, b, x, y;
    cin >> a >> b >> x >> y;
    a--;b--;
    vector<vector<P>> edges(200);
    rep(i,99){
        edges[i].emplace_back(i+1, y);
        edges[i+1].emplace_back(i, y);
        edges[i+100].emplace_back(i+101, y);
        edges[i+101].emplace_back(i+100, y);
    }
    rep(i,100){
        edges[i].emplace_back(i+100, x);
        edges[i+100].emplace_back(i, x);
    }
    rep(i,99){
        edges[i+100].emplace_back(i+1, x);
        edges[i+1].emplace_back(i+100, x);
    }
    queue<int> q;
    vector<int> dist(200, INF);
    dist[a] = 0;
    q.push(a);
    while(!q.empty()){
        int p = q.front();
        q.pop();
        for(auto c : edges[p]){
            if(dist[c.first] <= dist[p] + c.second)continue;
            dist[c.first] = dist[p] + c.second;
            q.push(c.first);
        }
    }
    cout << dist[b + 100] << endl;
    return 0;
}