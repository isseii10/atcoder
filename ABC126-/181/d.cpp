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
    string s; cin >> s;
    int n = s.size();
    vector<int> st_8_1;
    vector<pair<int, int>> st_8_2;
    vector<tuple<int, int, int>> st_8;
    map<int, int> mp_s;
    
    rep(i,n){
        mp_s[s[i]-'0']++;
    }
    /*
    ここがREの原因（なぜかはわからない）
    int s_int = stoi(s);
    rep(i,n){
        int keta_i = s_int%10;
        mp_s[keta_i]++;
        s_int /= 10;
    }
    */
    
    int eight = 8;
    while(eight < 1000){
        int simo_1, simo_2, simo_3;
        int eight_ = eight;
        simo_1 = eight_ % 10;
        eight_ /= 10;
        simo_2 = eight_ % 10;
        eight_ /= 10;
        simo_3 = eight_ % 10;
        if(eight < 10){
            st_8_1.push_back(simo_1);
        }
        if(eight < 100){
            st_8_2.push_back(make_pair(simo_2, simo_1));
        }
        st_8.push_back(make_tuple(simo_3, simo_2, simo_1));
        eight += 8;
    }
    bool yes_flag = false;
    map<int, int> mp_8;
    if(n == 1){
        if(stoi(s) == 8){
            yes_flag = true;
        }
    }
    else if(n == 2){
        for(auto p: st_8_2){
            mp_8[p.first]++;
            mp_8[p.second]++;
            if((mp_s[p.first] >= mp_8[p.first]) && (mp_s[p.second] >= mp_8[p.second])){
                yes_flag = true;
                break;
            }
            mp_8[p.first]--;
            mp_8[p.second]--;
        }
    }
    else{
        for (auto tpl : st_8){
            mp_8[get<0>(tpl)]++;
            mp_8[get<1>(tpl)]++;
            mp_8[get<2>(tpl)]++;
            if((mp_s[get<0>(tpl)] >= mp_8[get<0>(tpl)]) && (mp_s[get<1>(tpl)] >= mp_8[get<1>(tpl)]) && (mp_s[get<2>(tpl)] >= mp_8[get<2>(tpl)])){
                yes_flag = true;
                break;
            }
            mp_8[get<0>(tpl)]--;
            mp_8[get<1>(tpl)]--;
            mp_8[get<2>(tpl)]--;
        }
    }
    if(yes_flag) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}