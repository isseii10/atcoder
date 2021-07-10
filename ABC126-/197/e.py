import sys
from collections import OrderedDict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    c_x = OrderedDict()
    for _ in range(n):
        x, c = map(int, input().split())
        if c not in c_x.keys():
            c_x[c] = []
        c_x[c].append(x)
    #print(c_x)
    x_ = [[] for _ in range(n)]
    for c, l in c_x.items():
        l.sort()
        x_[c-1] = l



    balls = []
    for i in range(n):
        l = x_[i]
        if len(l) == 0:continue
        left, right = l[0], l[-1]
        balls.append((left, right))
    
    m = len(balls)
    dp = [[INF]*2 for _ in range(m+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    # dp[i][0] i番目に小さい色番まで回収し、左端にいる時の最小値
    # dp[i][1] i番目に小さい色番まで回収し、右端にいる時の最小値
    prev_l = 0
    prev_r = 0
    for i in range(m):
        l, r = balls[i]
        #i番目で左にいた時からの遷移
        if prev_l <= l:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + r-l + r-prev_l)
            dp[i+1][1] = min(dp[i+1][1], dp[i][0] + r-prev_l)
        elif l < prev_l <= r:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + r-l + r-prev_l)
            dp[i+1][1] = min(dp[i+1][1], dp[i][0] + r-l + prev_l-l)
        else:
            dp[i+1][0] = min(dp[i+1][0], dp[i][0] + prev_l-l)
            dp[i+1][1] = min(dp[i+1][1], dp[i][0] + prev_l-l + r-l)

        #i番目で右にいた時からの遷移
        if prev_r <= l:
            dp[i+1][0] = min(dp[i+1][0], dp[i][1] + r-l + r-prev_r)
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + r-prev_r)
        elif l < prev_r <= r:
            dp[i+1][0] = min(dp[i+1][0], dp[i][1] + r-l + r-prev_r)
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + r-l + prev_r-l)
        else:
            dp[i+1][0] = min(dp[i+1][0], dp[i][1] + prev_r-l)
            dp[i+1][1] = min(dp[i+1][1], dp[i][1] + prev_r-l + r-l)

        prev_r = r
        prev_l = l
    #print(balls)
    #print(prev_l, prev_r)
    #print(dp[m])
    ans = min(dp[m][0]+abs(balls[m-1][0]), dp[m][1]+abs(balls[m-1][1]))
    print(ans)
if __name__ == '__main__':
    main()