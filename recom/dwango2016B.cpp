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
    vector<int> k;
    rep(i,n-1){
        int ki; cin >> ki;
        k.push_back(ki);
    }
    vector<int> ans;
    ans.push_back(k[0]);
    rep(i,n-2){
        if(k[i] == k[i+1]){
            ans.push_back(k[i]);
            continue;
        }

        if(k[i] > k[i+1]){
            ans.push_back(k[i+1]);
        }
        else{
            ans.push_back(k[i]);
        }
    };
    ans.push_back(k[n-2]);
    for(auto a:ans){
        cout << a << " ";
    }
    cout << endl;
    return 0;
}