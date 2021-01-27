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

bool is_able(vector<int> a, int a_size){
    for(int i=0;i<a_size;i++){
        if(a[i] > i+1){
            return false;
        }
    }
    return true;
}

int main() {
    int n; cin >> n;
    vector<int> b(n);
    rep(i,n) cin >> b[i];
    if(!is_able){
        cout << -1 << endl;
        return 0;
    }
    
    return 0;
}