#include <bits/stdc++.h>
#define rep(i, n) for (int i=0; i < (n); i++)
using namespace std;
typedef long long ll;
typedef pair<int, int> P;

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> d(n);
    rep(i, n) cin >> d[i];
    int ans = 0;
    rep(left, n+1){
        rep(right, n+1){
            if(right + left > min(n, k))break;
            vector<int> hand(0, 0);
            for(int i=0;i<left;i++) hand.push_back(d[i]);
            for(int j=n-1;n-1 - right<j; j--)hand.push_back(d[j]);
            sort(hand.begin(), hand.end());
            int back = k;
            back -= left + right;
            int hand_n = hand.size();
            int res = 0;
            rep(i, hand_n){
                if (hand[i] < 0 && back > 0){
                    back--;
                    continue;
                };
                res += hand[i];
            }
            ans = max(ans, res);
        }

    };
    cout << ans << endl;
}