#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int r, D, x;
    cin >> r >> D >> x;
    rep(i, 10){
        x = r*x - D;
        cout << x << endl;
    }
}