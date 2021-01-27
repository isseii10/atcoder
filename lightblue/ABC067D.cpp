
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
    int n;
    cin >> n;
    vector<vector<int>> edges(n);
    rep(i,n-1){
        int a, b;
        cin >> a >> b;
        a--; b--;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }
    vector<int> dist(n, -1);
    vector<int> parent(n);
    //最短経路
    queue<int> q;
    q.push(0);
    dist[0] = 0;
    parent[0] = -1;
    while (!q.empty()){
        int p = q.front();
        q.pop();
        for(auto c : edges[p]){
            if (dist[c] != -1) continue;
            dist[c] = dist[p] + 1;
            parent[c] = p;
            q.push(c);
        }
    }
    //最短経路復元
    vector<int> shortestPath;
    shortestPath.push_back(n-1);
    int p = n-1;
    while(parent[p]!= -1){
        shortestPath.push_back(parent[p]);
        p = parent[p];
    }
    int ss = shortestPath.size();
    int fennec = ss/2;
    if(ss%2 != 0) fennec += 1;
    vector<int> black, white;
    while (!shortestPath.empty())
    {
        if(fennec!=0) {
            black.push_back(shortestPath.back());
            shortestPath.pop_back(); fennec--;
            continue;
        }
        white.push_back(shortestPath.back());
        shortestPath.pop_back();
    }
    //ノードに色塗りして再度bfs
    vector<int> collor(n, -1);
    for(auto b : black) collor[b] = 1;
    for(auto w : white) collor[w] = 2;
    queue<int> d;
    rep(i,n) if(collor[i]!=-1) d.push(i);
    while(!d.empty()){
        p = d.front();
        d.pop();
        for (auto c : edges[p]){
            if (collor[c]!=-1) continue;
            collor[c] = collor[p];
            d.push(c);
        }
    }
    int black_count=0, white_count=0;
    for(int j=0;j<n;j++){
        if(collor[j]==1)black_count++;
        else white_count++;
    }
    if (black_count > white_count) cout << "Fennec" << endl;
    else cout << "Snuke" << endl; 
    
    return 0;
}
