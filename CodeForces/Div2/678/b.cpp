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
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<deque<int>> ans;
        int l = n-2;
        int r = 0;
        for(int i=0;i<n-1;i++){
            deque<int> row;
            row.push_back(1);
            row.push_back(1);

            for(int j=0;j<l;j++){
                row.push_front(0);
            }
            for(int k=0;k<r;k++){
                row.push_back(0);
            }
            ans.push_back(row);
            l--;
            r++;
        }
        deque<int> last_row;
        for(int i=0;i<n-2;i++){
            last_row.push_back(0);
        }
        last_row.push_front(1);
        last_row.push_back(1);
        ans.push_back(last_row);
        
        rep(i,n){
            for(auto x : ans[i]){
                cout << x << " ";
            }
            cout << endl;
        }
    }
    return 0;
}