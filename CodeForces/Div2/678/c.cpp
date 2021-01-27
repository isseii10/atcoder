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
    int n, x, pos; cin >> n >> x >> pos;

    //binarysarch
    int l = 0;
    int r = n;
    ll res = 1;
    int count = 1;
    int l_count = 0;
    int r_count = 0;
    while(l<r){
        int mid = (l+r)/2;
        if(mid < pos){
            l = mid + 1;
            //idx midにある値はｘ以下.ｘ以外のｘ－１通り
            res = res * (x-1 - l_count) % MOD;
            l_count++;
        }
        else if(mid==pos){
            l = mid + 1;
        }
        else{
            r = mid;
            res = res*(n-x - r_count) %MOD;
            r_count++;
        }
        count++;
    }
    for(int i=1;i<=n-count+1;i++)
        res = res*i % MOD;
    cout << res << endl;
    return 0;
}