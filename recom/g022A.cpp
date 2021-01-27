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
    vector<int> alph(26, 0);
    for(auto c : s)alph[c-'a']++;
    
    if(n<26){
        rep(i,26){
            if(alph[i]==0){
                char a = i + 'a';
                cout << s << a << endl;
                return 0;
            }
        }
    }
    else{
        vector<char> s_tail;
        char out;
        string sbstr;
        bool out_flag = false;
        for(int i = n-1;i>=1;i--){
            if(s[i]-'a' < s[i-1] - 'a'){
                s_tail.push_back(s[i]);
                if(i-1==0){
                    out_flag = true;
                }
            }
            else{
                s_tail.push_back(s[i]);
                out = s[i-1];
                sbstr = s.substr(0, i-1);
                break;
            }
        }

        if(out_flag){
            cout << -1 << endl;
            return 0;
        }

        sort(s_tail.begin(), s_tail.end());
        int idx = lower_bound(s_tail.begin(), s_tail.end(), out)-s_tail.begin();
        //cout << s_tail[idx] << endl;

        cout << sbstr << s_tail[idx] << endl;

    }
    return 0;
}