import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    dp = [[0]*(b+1) for _ in range(a+1)]
    # dp1[i][j] Aの山、Bの山の一番上のカードがそれぞれi,jの時から最終状態に行くまでに取るすぬけの点数

    for i in range(a+1)[::-1]:
        for j in range(b+1)[::-1]:

            if (i+j) % 2 == 0:
                if i == a and j == b:
                    dp[i][j] = 0
                elif i == a:
                    dp[i][j] = dp[i][j+1]+Bs[j]
                elif j == b:
                    dp[i][j] = dp[i+1][j]+As[i]
                else:
                    dp[i][j] = max(dp[i+1][j]+As[i], dp[i][j+1]+Bs[j])
            else:
                if i == a and j == b:
                    dp[i][j] = 0
                elif i == a:
                    dp[i][j] = dp[i][j+1]
                elif j == b:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j+1]) 
    print(dp[0][0])

if __name__ == '__main__':
    main()