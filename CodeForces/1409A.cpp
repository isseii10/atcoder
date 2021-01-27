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
    int t;
    cin >> t;
    rep(i,t){
        int a, b;
        cin >> a >> b;
        if(b>=a){
            int count = (b-a) / 10 + 1;
            if ((b-a)%10==0) count--;
            cout << count << endl;
        }
        else{
            int count = (a-b) / 10 + 1;
            if((a-b)%10==0) count--;
            cout << count << endl;
        }
    }
    return 0;
}