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
    int a[6];
    rep(i,6) cin >> a[i];
    int n; cin >> n;
    int b[n];
    rep(i,n) cin >> b[i];

    vector<int> max_flet(6, 0);
    vector<int> min_flet(6, INF);

    for(int i=0;i<6;i++){
        for(auto bi : b){
            max_flet[i] = max(max_flet[i], bi-a[i]);
            min_flet[i] = min(min_flet[i], bi-a[i]);
        }
    }
    int left = INF;
    int right = 0;
    for(int i=0;i<6;i++){
        left = min(left, max_flet[i]);
        right = max(right, min_flet[i]); 
    }
    cout << left-right << endl;
    

    return 0;
}