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
    int m, k;
    cin >> m >> k;
    if(m==0){
        if(k==0){
            cout << 0 << " " << 0 << endl;
            return 0;
        }
        else{
            cout << -1 << endl;
            return 0;
        }
    }

    if(m==1 && k == 1){
        cout << -1 << endl;
        return 0;
    }

    if(k>=(1<<m)){
        cout << -1 << endl;
        return 0;
    }
    deque<int> ans;
    if(k!=0){
        ans.push_front(k);
        for(int i=0; i<(1<<m);i++){
            if(i==k)continue;
            ans.push_back(i);
            ans.push_front(i);
        }
        ans.push_front(k);
    }else{
        for(int i=0;i<(1<<m);i++){
            ans.push_front(i);
            ans.push_front(i);
        }
    }
    rep(i,(int)ans.size()){
        if(i!=(int)ans.size()-1)
            cout << ans[i] << " ";
        else cout << ans[i] << endl;
    }
    return 0;
}