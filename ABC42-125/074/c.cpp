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
    int a, b, c, d, e, f;
    cin >>a>>b>>c>>d>>e>>f;
    int count1, count2, count3, count4;
    count1 = f/(100*a);
    count2 = f/(100*b);
    count3 = f/c;
    count4 = f/d;
    double res = 0;
    P ans = make_pair(0, 0);
    for(int i=0;i<=count1;i++){
        for(int j=0;j<=count2;j++){
            int water = 100*a*i + 100*b*j;
            if(water > f) continue;
            for(int k=0;k<=count3;k++){
                for(int l=0;l<=count4;l++){
                    int sugar = k*c + l*d;
                    if(sugar + water > f || sugar+water == 0 || sugar > water/100*e)continue;
                    double nodo = static_cast<double>(sugar)/static_cast<double>(sugar+water) * 100;
                    if(res < nodo){
                        ans.first = sugar+water;
                        ans.second = sugar;
                    }
                }
            }            
        }
    }
    cout << ans.first << " " << ans.second << endl;
    return 0;
}