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
    string s;
    cin >> s;
    string s1 = s.substr(0, 2);
    string s2 = s.substr(2, 2);
    int s1_i = stoi(s1);
    int s2_i = stoi(s2);
    bool yflag1 = false;
    bool yflag2 = false;
    if(s1_i == 0 || s1_i >= 13)yflag1 = true;
    if(s2_i == 0 || s2_i >= 13)yflag2 = true;
    if(yflag1 && yflag2){
        cout << "NA" << endl;
    }
    else if(yflag1 && !yflag2){
        cout << "YYMM" << endl;
    }else if(!yflag1 && yflag2){
        cout << "MMYY" << endl;
    }else{
        cout << "AMBIGUOUS" << endl;
    }
    return 0;
}