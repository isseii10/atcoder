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
    int n, k;
    cin >> n >> k;
    set<P> edges;
    for (int i = 2;i<=n;i++){
        edges.insert(make_pair(1, i));
    };
    int dist_2 = ((n-1)*(n-2))/2;
    if (k > dist_2) cout << -1 << endl;
    else{
        int count = dist_2 - k; 
        if (count > 0){
            bool ok = false;
            for (int i = 2; i<=n-1;i++){
                for (int j = i+1;j<=n;j++){
                    if(i==j)continue;
                    P p = make_pair(i, j);
                    edges.insert(p);
                    count--;
                    if (count == 0){
                        ok = true;
                        break;
                    }
                };
                if(ok)break;
            }
        };
        cout << edges.size() << endl;
        for (auto x : edges) cout << x.first << " " << x.second << endl;
    }
    return 0;
}