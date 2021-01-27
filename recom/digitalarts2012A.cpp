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
    string s; getline(cin, s);
    int s_size = s.size();
    vector<string> ss;
    string tmp = "";
    rep(i,s_size){
        if(s[i]!= ' ')
            tmp += s[i];
        else{
            ss.push_back(tmp);
            tmp.clear();
        }
    }
    if(!tmp.empty())
        ss.push_back(tmp);

    int n; cin >> n;
    map<int, vector<string>> ngs;
    rep(i,n){
        string t; cin >> t;
        ngs[t.size()].push_back(t);
    }
    string ans = "";
    for(auto x:ss){
        int x_size = x.size();
        if (ngs[x_size].empty()){
            ans += x;
            ans += ' ';
        }
        else{
            for(auto ng :ngs[x_size]){
                bool ngflag = true;
                rep(i,x_size){
                    if(ng[i]=='*')continue;
                    if(ng[i] != x[i])ngflag = false;
                }
                if(ngflag){
                    rep(j, x_size)
                        ans += '*';
                    ans += ' ';
                }
                else{
                    ans += x;
                    ans += ' ';
                }
            }
        }
    }
    cout << ans << endl;

    return 0;
}