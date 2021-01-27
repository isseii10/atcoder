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

//BIT 1-indexed
class BIT{
public:
    ll n;
    vector<ll> bit;
    BIT(ll _n) : n(_n), bit(_n+1, 0){}

    /*
    addとsumはうまく動くのを確認したが
    maxをとるset_valueとmax_valueは自作なので不安
    */


    void add_value(ll i, ll x){
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k & -k)){
            bit[k] += x;
        }
    }

    

    ll sum_value(ll i){
        ll s = 0;
        if(i==0) return s;
        for(ll k=i;k>0;k-=(k&-k)){
            s += bit[k];
        }
        return s;
    }

    void set_value(ll i, ll x){
        //区間maxをとるためのset_value
        //区間minなら書き換え
        if(i==0) return;
        for(ll k=i;k<=n;k+=(k&-k)){
            bit[k] = max(bit[k], x);
        }
    }

    ll max_value(ll i){
        ll m = 0; // 全部正の数なら０
        if(i==0) return m;
        for(ll k=i;k>0;k-=(k&-k)){
            m = max(m, bit[k]);
        }
        return m;
    }

};

int main() {
    int n = 8;
    BIT bit(n);
    for(int i=1;i<=n;i++){
        cout << bit.bit[i] << " ";
    }
    cout <<endl;

    for(int i=1;i<=n;i++){
        bit.set_value(i, i);
    }
    for(int i=1;i<=n;i++){
        cout << bit.bit[i] << " ";
    }
    cout <<endl;

    bit.set_value(5, 80);

    for(int i=1;i<=n;i++){
        cout << bit.bit[i] << " ";
    }
    cout <<endl;
    for(int i=1;i<=n;i++){
        cout << bit.sum_value(i) << " ";
    }
    cout <<endl;




    return 0;
}