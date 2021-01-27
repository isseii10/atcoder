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

vector<map<char, int>> dict(5010);

int main() {
    int n; cin >> n;
    string s; cin >> s;

    vector<string> ss(n+1, "");
    
    for (int i=0;i<n;i++){
        ss[i+1] = ss[i] + s[i];
    }
    for (int i=1;i<=n;i++){
        for (auto c : ss[i]){
            dict[i][c] += 1;
        }
    }
    
    int ans = 0;
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n+1;j++){
            
            if (dict[j]['T']-dict[i]['T'] == dict[j]['A']-dict[i]['A'] && dict[j]['C']-dict[i]['C'] == dict[j]['G']-dict[i]['G'])
                ans += 1;
        }
    }
    cout << ans << endl;
    

    return 0;
}