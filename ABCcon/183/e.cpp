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
    int h, w; cin >> h >> w;
    vector<string> table(h);
    rep(i,h) cin >> table[i];
    vector<vector<ll>> move_s(h, vector<ll>(w, 0));
    bool h_flag = false;
    rep(i,h){
        if(i==0)continue;
        if(table[i][0] == '#'){
            move_s[i][0] = 0;
            h_flag = true;
        }
        else{
            if(h_flag)break;
            move_s[i][0] = 1;
        }
    }
    bool w_flag = false;
    rep(i,w){
        if(i==0)continue;
        if(table[0][i] == '#'){
            move_s[0][i] = 0;
            w_flag = true;
        }
        else{
            if(w_flag)break;
            move_s[0][i] = 1;
        }
    }
    bool naname_flag = false;
    rep(i, min(h, w)){
        if(i==0)continue;
        if(table[i][i] == '#'){
            move_s[i][i] = 0;
            naname_flag = true;
        }
        else{
            if(naname_flag)break;
            move_s[i][i] = 1;
        }
    }
    /*
    rep(i, h){
        rep(j,w){
            cout << move_s[i][j];
        }
        cout << endl;
    }*/
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(table[i][j]=='#')continue;
            if(i==0 && j==0)continue;
            else if(i==0 && j!=0){
                move_s[i][j] = (move_s[i][j] + move_s[i][j-1]) %MOD;
            }
            else if(i!=0 && j==0){
                move_s[i][j] = (move_s[i][j] + move_s[i-1][j]) %MOD;
            }
            else if (i!=0 && j!=0){
                move_s[i][j] = (move_s[i][j] + move_s[i-1][j] + move_s[i][j-1] + move_s[i-1][j-1])%MOD;
            }
        }
    }
    cout << move_s[h-1][w-1] << endl;
    return 0;
}