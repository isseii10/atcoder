import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n, m, k = map(int, input().split())
    dp = [[0]*(m+1) for _ in range(n)]
    #dp[i][m] := iまでで、a[i]がmで条件を満たす数
    for j in range(1, m+1):
        dp[0][j] = 1
    dp_sum = [[0]*(m+1) for _ in range(n)]
    dp_sum[0][1] = 1 
    for j in range(1, m+1):
        dp_sum[0][j] = 1
        dp_sum[0][j] += dp_sum[0][j-1]
        dp_sum[0][j] %= MOD
        
    for i in range(1, n):
        for j in range(1, m+1):
            if k == 0:
                dp[i][j] += dp_sum[i-1][m] 
                dp[i][j] %= MOD
            else:
                dp[i][j] = dp_sum[i-1][m] + dp_sum[i-1][max(j-k, 0)] - dp_sum[i-1][min(j+k-1, m)]
                dp[i][j] %= MOD

            dp_sum[i][j] = dp[i][j] + dp_sum[i][j-1] 
            dp_sum[j][j] %= MOD
            
    print(sum(dp[n-1])%MOD)
if __name__ == '__main__':
    main()