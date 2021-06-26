import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    t = list(map(int, input().split()))
    m = sum(t)
    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    #dp[i][t]:= i番目までの料理を作るのにオーブン１でかかる時間がtの時の、オーブン2でかかる時間

    for i in range(n):
        time = t[i]
        for j in range(m):
            #オーブン1で作るとき
            if j + time < m:
                dp[i+1][j+time] = dp[i][j]
            #オーブン２で作る時
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+time)
    
    ans = INF
    for t in range(m):
        if dp[n][t] == INF:continue
        ans = min(ans, max(t, dp[n][t]))
    print(ans)


if __name__ == '__main__':
    main()