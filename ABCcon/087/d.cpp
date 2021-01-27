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
    int n, m; cin >> n >> m;
    vector<vector<P>> edge(n, vector<P>(0));
    rep(i,m){
        int l, r, d;
        cin >> l >> r >> d;
        l--; r--;
        edge[l].emplace_back(r, d);
        edge[r].emplace_back(l, -d);
    }
    vector<bool> visited(n, false);
    stack<int> st;
    vector<int> x(n,-1);
    rep(i,n){
        if(visited[i])continue;
        st.push(i);
        visited[i] = true;
        x[i] = 0;
        while(!st.empty()){
            int p = st.top();
            st.pop();
            for(auto c : edge[p]){
                if(visited[c.first]){
                    if(x[c.first]!=x[p]+c.second){
                        cout << "No" << endl;
                        return 0;
                    }
                    else continue;
                }
                st.push(c.first);
                visited[c.first] = true;
                x[c.first] = x[p] + c.second;
            }
        }
    }
    cout << "Yes" << endl;
    return 0;
}