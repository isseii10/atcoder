import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)
    ab = sorted(zip(a, b))
    #print(ab)

    dp = [[[0]*(2) for _ in range(a_max+1)] for _ in range(n+1)]
    #dp[i][s][flag]は、i番目まででbの合計がsである選び方の場合の数(a[i]を選んでいるかどうかをflagで管理する)
    dp[0][0][0] = 1
    ans = 0
    for i in range(n):
        ai, bi = ab[i]
        for j in range(a_max+1):
            #iを選ばない時
            dp[i+1][j][0] = (dp[i][j][1] + dp[i][j][0]) % MOD
            #iを選ぶ時
            if j-bi >= 0:
                dp[i+1][j][1] = (dp[i][j-bi][1] + dp[i][j-bi][0]) % MOD
            if j <= ai:
                ans += dp[i+1][j][1]
                ans %= MOD

    print(ans)




if __name__ == '__main__':
    main()