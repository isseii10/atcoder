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
    int n, k; cin >> n >> k;
    vector<vector<int>> edge(n);
    rep(i, n-1){
        int a, b;
        cin >> a >> b;
        a--;b--;
        edge[a].push_back(b);
        edge[b].push_back(a);
    }
    vector<int> colored(n, -1);
    queue<int> q;
    q.push(0);
    colored[0] = k;
    int pp = -1;
    while(!q.empty()){
        int p = q.front();
        q.pop();
        int count = 0;
        for(auto c : edge[p]){
            if(colored[c]!=-1)continue;
            if(pp == -1)
                colored[c] = k-1-count;
            else
                colored[c] = k-2-count;
            q.push(c);
            count++;
        }
        pp = p;
    }
    
    ll ans = 1;
    rep(i,n){
        ans = ans*colored[i] % MOD;
    }
    cout << ans << endl;
    return 0;
}