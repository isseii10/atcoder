#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int h, w;
    cin >> h >> w;
    vector<string> grid(h);
    rep(i, h) cin >> grid[i];
    //右から累積和
    int s_right[h][w+1];
    //左から累積和
    int s_left[h][w+1];
    rep(i, h){
        s_right[i][w] = 0; //wは 0-index
        s_left[i][0] = 0; //wは 1-index
        for(int j=w;j>0;j--){
            if(grid[i][j-1] == '.')s_right[i][j-1] = s_right[i][j] + 1;
            else s_right[i][j-1] = 0;
        };
        for (int j=0;j<w;j++){
            if(grid[i][j] == '.')s_left[i][j+1] = s_left[i][j] + 1;
            else s_left[i][j+1] = 0;
        };
    };
    int s_up[h+1][w];
    int s_down[h+1][w];
    rep(j, w){
        s_up[0][j] = 0; // hは1-indexed
        s_down[h][j] = 0; //hは0-indexed
        for(int i=h;i>0;i--){
            if(grid[i-1][j]=='.')s_down[i-1][j] = s_down[i][j] + 1;
            else s_down[i-1][j] = 0;
        };
        for(int i=0;i<h;i++){
            if(grid[i][j] == '.')s_up[i+1][j] = s_up[i][j] + 1;
            else s_up[i+1][j] = 0;
        };  
    };
    int ans = 0;
    rep(i, h)rep(j, w){
        int res = 0;
        res += s_up[i+1][j];
        res += s_down[i][j];
        res += s_left[i][j+1];
        res += s_right[i][j];
        res -= 3;
        ans = max(ans, res);
    };
    cout << ans << endl;
}