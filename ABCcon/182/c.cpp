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
    string n; cin >> n;
    int n_sz = n.size();
    ll res = 0;
    vector<ll> mod_3(3, 0);
    for(auto c: n){
        int tmp = (c-'0')%3;
        mod_3[tmp]++;
        res += tmp;
    }
    if(res%3==0){
        cout << 0 << endl;
    }
    else if(res%3==1){
        if(mod_3[1]>0){
            if(n_sz > 1)
                cout << 1 << endl;
            else
            {
                cout << -1 << endl;
            }
            
        }
        else{
            if(mod_3[2]>=2){
                if(n_sz>2)
                    cout << 2 << endl;
                else
                    cout << -1 <<endl;
            }
            else{
                cout << -1 << endl;
            }
        }
    }
    else if(res%3==2){
        if(mod_3[2]>0){
            if(n_sz > 1)
                cout << 1 << endl;
            else
            {
                cout << -1 << endl;
            }
        }
        else{
            if(mod_3[1]>=2){
                if(n_sz>2)
                    cout << 2 << endl;
                else
                    cout << -1 <<endl;
            }
            else{
                cout << -1 << endl;
            }
        }
    }

    return 0;
}