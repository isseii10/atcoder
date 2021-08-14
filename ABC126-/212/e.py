import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n, m, K = map(int, input().split())
    non_edges = [[]*n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        non_edges[u].append(v)
        non_edges[v].append(u)
    
    dp = [[0]*n for _ in range(K+1)]
    #dp[k][i] は、k日目に都市iにいるときの場合の数
    dp[0][0] = 1

    sum_dp = [0]*(K+1)
    sum_dp[0] = 1

    for k in range(K):

        for i in range(n):
            dp[k+1][i] = (sum_dp[k] - dp[k][i]) % MOD
            for j in non_edges[i]:
                dp[k+1][i] -= dp[k][j]
                dp[k+1][i] %= MOD

            sum_dp[k+1] += dp[k+1][i]
            sum_dp[k+1] %= MOD

# L30 ~ L37はO(n+m)になるぽい　よく分からん 

    print(dp[K][0])

    

if __name__ == '__main__':
    main()