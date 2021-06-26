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

bool is_seven_in_ten(int x){
    while(x!=0){
        if(x % 10 == 7)
            return true;
        else{
            x /= 10;
        }
    }
    return false;
}

bool is_seven_in_eight(int x){
    while(x!=0){
        if(x % 8 == 7){
            return true;
        }
        else{
            x /= 8;
        }
    }
    return false;
}

int main() {
    int n; cin >> n;
    int ten = 0, eight = 0, ten_eight = 0;
    for(int i=1;i<=n;i++){
        if(is_seven_in_eight(i) && is_seven_in_ten(i)){
            ten_eight++;
        }
        if(is_seven_in_ten(i)){
            ten++;
        }
        if(is_seven_in_eight(i)){
            eight++;
        }
    }
    
    cout << n - ten - eight + ten_eight << endl;
    return 0;
}