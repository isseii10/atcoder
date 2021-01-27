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

//bellman-ford
struct edge{
    int from, to;
    ll cost;
};
    // 嘘解法１３７E
vector<ll> cost(3000);
//始点から到達可能でかつ終点へ到達可能な不閉路が検出されたらfalse、そうでないならtrue
bool bellman_ford(int n, const vector<edge> &es, int s, int g){
    cost.assign(n, INF);
    cost[s] = 0;
 
    rep(i, n){
        for(auto &e : es){
            if(cost[e.from] < INF && cost[e.from] + e.cost < cost[e.to]){
                if(i >= n - 1 && e.to == g)return false;
                else if(i >= n - 1)cost[e.to] = -INF;
                else cost[e.to] = cost[e.from] + e.cost;
            }
        }
    }
    return true;
}

int main() {

    return 0;
}