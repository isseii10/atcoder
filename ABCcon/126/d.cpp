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
    vector<vector<P>> edges(n, vector<P>(0));
    rep(i,n-1){
        int u, v, w;
        cin >> u >> v >> w;
        u--;v--;
        edges[u].emplace_back(v,w);
        edges[v].emplace_back(u,w);
    }
    vector<int> collor(n, 0);
    vector<bool> visited(n, false);
    stack<int> st;
    st.push(0);
    collor[0] = -1;
    visited[0] = true;
    while(!st.empty()){
        int p = st.top();
        st.pop();
        for(auto c:edges[p]){
            if(visited[c.first])continue;
            st.push(c.first);
            visited[c.first] = true;
            if(c.second%2==0){
                collor[c.first] = collor[p];
            }
            else{
                collor[c.first] = -1 * collor[p];
            }
        }
    }
    rep(i,n){
        if(collor[i]==-1)cout << 0 << endl;
        else cout << 1 << endl;
    }
    return 0;
}