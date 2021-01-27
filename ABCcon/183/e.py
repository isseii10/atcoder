#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
inf = float('inf')

def main():
    mod = 10**9+7
    h, w = map(int, input().split())
    grid = [input()[:-1] for _ in range(h)]
    #print(grid)

    #dp[i][j] = dp[i][j-1] + dp[i][j-2] + ...
    #         + dp[i-1][j] + dp[i-2][j] + ... 
    #         + dp[i-1][j-1] + dp[i-2][j-2] + ...
    #という遷移なので、上からこれるやつ(dp_u)、左からこれるやつ(dp_l)、左上からこれるやつ(dp_ul)を累積和とる
    dp = [[0]*(w+1) for _ in range(h+1)]
    dp_u = [[0]*(w+1) for _ in range(h+1)]
    dp_l = [[0]*(w+1) for _ in range(h+1)]
    dp_ul = [[0]*(w+1) for _ in range(h+1)]

    for i in range(1, h+1):
        for j in range(1, w+1):
            if i==1 and j==1: dp[i][j] = 1
            dp[i][j] += dp_u[i-1][j]
            dp[i][j] += dp_l[i][j-1]
            dp[i][j] += dp_ul[i-1][j-1]
            dp[i][j] %= mod

            dp_u[i][j] = (dp_u[i-1][j] + dp[i][j]) % mod
            dp_l[i][j] = (dp_l[i][j-1] + dp[i][j]) % mod 
            dp_ul[i][j] = (dp_ul[i-1][j-1] + dp[i][j]) % mod

            if grid[i-1][j-1] == '#':
                dp[i][j] = 0
                dp_u[i][j] = 0
                dp_l[i][j] = 0
                dp_ul[i][j] = 0

    print(dp[h][w])

if __name__ == '__main__':
    main()