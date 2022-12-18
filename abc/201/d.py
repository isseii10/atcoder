import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    A = [input()[:-1] for _ in range(h)]

    a = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            a[i][j] = 1 if A[i][j] == "+" else -1

    #dp[i][j]は(i,j)から最終局面に行くときの高橋ー青木のスコア
    dp = [[0]*(w) for _ in range(h)]

    #初期化
    for i in range(h):
        for j in range(w):
            if (i+j)%2 == 0:
                dp[i][j] = -INF
            else:
                dp[i][j] = INF

    dp[h-1][w-1] = 0

    for i in range(h)[::-1]:
        for j in range(w)[::-1]:
            if i > 0:
                if (i-1+j) % 2 == 0:
                    #takahashi
                    dp[i-1][j] = max(dp[i-1][j], dp[i][j] + a[i][j])
                else:
                    #aoki
                    dp[i-1][j] = min(dp[i-1][j], dp[i][j] - a[i][j])
            
            if j > 0:
                if (i+j-1) % 2 == 0:
                    #takahashi
                    dp[i][j-1] = max(dp[i][j-1], dp[i][j] + a[i][j])
                else:
                    #aoki
                    dp[i][j-1] = min(dp[i][j-1], dp[i][j] - a[i][j])
    
    #print("==========================")
    #for i in range(h):
    #    print(dp[i])
    #print("==========================")

    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")

    
if __name__ == '__main__':
    main()