#include <bits/stdc++.h>
//#include <atcoder/all>
#define rep(i, n) for (int i=0; i < (int)(n); i++)
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
    int n = (int)s.size();
    P goal;
    cin >> goal.first >> goal.second;
    int count_t = 0;
    int move_dist_x = 0, move_dist_y = 0;
    vector<int> move_y;
    deque<int> move_x;
    rep(i,n){
        if(s[i]=='T'){
            count_t++;
            if(move_dist_y!=0){
                move_y.push_back(move_dist_y);
                move_dist_y = 0;
            }
            if(move_dist_x!=0){
                move_x.push_back(move_dist_x);
                move_dist_x = 0;
            }
        }
        else{
            if(count_t%2==0)
                move_dist_x++;
            else
                move_dist_y++;
        }
    }
    if(move_dist_y!=0)move_y.push_back(move_dist_y);
    if(move_dist_x!=0)move_x.push_back(move_dist_x);
    
    if(s[0] == 'F') //このときはx座標の正の方向しか進めない
    {
        goal.first -= move_x.front();
        move_x.pop_front();
    }
    //if(goal.first < 0) goal.first = -goal.first;
    //if(goal.first < 0) goal.second = -goal.second;

    //ここからdp
    int n_x = (int)move_x.size();
    int n_y = (int)move_y.size(); 
    vector<vector<bool>> dp_x(n_x+1, vector<bool>(16010, false));
    vector<vector<bool>> dp_y(n_y+1, vector<bool>(16001, false));
    dp_x[0][8000] = true;
    dp_y[0][8000] = true;
    rep(i, n_x){
        for(int j=0;j<16001;j++){
            if(dp_x[i][j]){
                dp_x[i+1][j-move_x[i]] = true;
                dp_x[i+1][j+move_x[i]] = true;
            }
            /*
            bool from_minus = false;
            bool from_plus = false;
            if(j-move_x[i]>=0) from_minus = dp_x[i][j-move_x[i]];
            if(j+move_x[i]<16001) from_plus = dp_x[i][j+move_x[i]];
            dp_x[i+1][j] = from_minus || from_plus;
            */
        }
    }
    rep(i, n_y){
        for(int j=0;j<16001;j++){
            if(dp_y[i][j]){
                dp_y[i+1][j-move_y[i]] = true;
                dp_y[i+1][j+move_y[i]] = true;
            }
            /*
            bool from_minus = false;
            bool from_plus = false;
            if(j-move_y[i]>=0) from_minus = dp_y[i][j-move_y[i]];
            if(j+move_y[i]<16001) from_plus = dp_y[i][j+move_y[i]];
            dp_y[i+1][j] = from_minus || from_plus;
            */
        }
    }
     
    //例えばs.size()が8000で全てFのとき、
    //goal.firstは-8000される(50～54行目くらい)
    //このとき、目標がもともとマイナスだったら、
    //dp_x[n_x][goal.first + 8000]はout of rangeなのでREになる。
    if(goal.first <= -8000)
    { 
        cout << "No" << endl;
        return 0;
    }
    if(dp_x[n_x][goal.first + 8000] && dp_y[n_y][goal.second + 8000])
        cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}