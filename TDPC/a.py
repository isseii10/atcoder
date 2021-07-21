import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    p = list(map(int, input().split()))
    dp = [[False]*(sum(p)+1) for _ in range(n+1)]
    #dp[i][score]はi番目までの問題でスコアがscoreになる場合の数
    dp[0][0] = True

    for i in range(n):
        score = p[i]
        dp[i+1][score] = True
        for s in range(sum(p)):
            dp[i+1][s] = (dp[i+1][s] or dp[i][s])
            if s + score <= sum(p):
                dp[i+1][s+score] = dp[i+1][s+score] or dp[i][s]

    #for i in range(n+1):
    #    print(dp[i])
    print(sum(dp[n]))

if __name__ == '__main__':
    main()