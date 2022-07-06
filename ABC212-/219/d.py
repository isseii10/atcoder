import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    X, Y = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    dp = [[[INF]*(Y+1) for _ in range(X+1)] for _ in range(n+1)]
    dp[0][0][0] = 0
    #dp[i][x][y]は、i番目までの弁当で、たこ焼きをx個,たい焼きをy個かったときの最小の値段
    for i in range(n):
        a, b = ab[i]
        for x in range(X+1):
            for y in range(Y+1):
                #i番目は買わない
                dp[i+1][x][y] = min(dp[i+1][x][y], dp[i][x][y])
                #買う
                dp[i+1][min(X, x+a)][min(Y, y+b)] = min(dp[i+1][min(X, x+a)][min(Y, y+b)], dp[i][x][y]+1)
    if dp[n][X][Y] == INF:
        print(-1)
    else:
        print(dp[n][X][Y])

if __name__ == '__main__':
    main()