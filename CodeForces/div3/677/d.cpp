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

struct district
{
    ll num;
    ll gang;
};

vector<P> build(vector<ll> a, int a_size){
    int a_0 = a[0];
    vector<P> road;
    int to = -1;
    for(int i=1;i<a_size;i++){
        if(a[i]!=a_0){
            road.emplace_back(1, i+1);
            to = i;
        }
    }
    if(to==-1){
        return road;
    }
    else{
        if(road.size()==a_size-1){
            return road;
        }
        else{
            for(int i=1;i<a_size;i++){
                if(a[i]==a_0){
                    road.emplace_back(to+1, i+1);
                }
            }
            return road;
        }
    }
}


int main() {
    int t; cin >> t;
    while(t--){
        int n; cin >> n;
        vector<ll> a(n);
        rep(i,n){
            cin >> a[i];
        }
        vector<P> road;
        road = build(a, n);
        if(road.size()==0){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << endl;
            for(auto p:road){
                cout << p.first << " " << p.second << endl;
            }
        }


    }
    return 0;
}