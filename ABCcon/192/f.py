import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, x = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [[0]*(n+5) for _ in range(n+5)]

    ans = INF
    for k in range(1, n+1):
        #k種類使う

        #初期化
        for i in range(k+1):
            for j in range(k):
                dp[i][j] = -INF
        dp[0][0] = 0

        #更新
        for a in A:
            for i in range(k)[::-1]:
                for j in range(k):
                    dp[i+1][(j + a)%k] = max(dp[i+1][(j+a)%k], dp[i][j] + a)

        s = dp[k][x%k]
        if s < 0:continue
        ans = min(ans, (x-s)//k)
    print(ans)


if __name__ == '__main__':
    main()