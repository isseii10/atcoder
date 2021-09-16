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

char result[105][105];

int main() {
    int n, k; cin >> n >> k;
    string s; cin >> s;
    for(int width = 1; width <= k+2; width++){
        for(int l = 0; l+width <= k+2; l++){
            int r = l+width;
            if(r-l == 1){
                result[l][r] = s[l%n];
                cout << result[l][r] << endl;
            }
            else{
                int mid = (l+r)/2;
                if(result[l][mid] == 'R' && result[mid][r] == 'P')
                    result[l][r] = result[mid][r];
                else if(result[l][mid] == 'S' && result[mid][r] == 'R')
                    result[l][r] = result[mid][r];
                else if(result[l][mid] == 'P' && result[mid][r] == 'S')
                    result[l][r] = result[mid][r];
                else
                    result[l][r] = result[l][mid];
            }
        }
    }
    cout << result[0][k+1] << endl;
    return 0;
}