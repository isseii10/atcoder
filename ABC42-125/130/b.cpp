#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
//using namespace atcoder;
typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef pair<int, int> P;

int main() {
    int n, x;
    cin >> n >> x;
    int l[n];
    rep(i, n) cin >> l[i];
    int count = 1;
    int now = 0;
    rep(i, n){
        now += l[i];
        if (x < now)break;
        count += 1;
    }
    cout << count << endl;
}