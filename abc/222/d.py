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

    dp = [[0]*3001 for _ in range(n)]
    #dp[i][x]はciをxとした時の広義短調増加列の数 (途中で累積和とる方針にした)

    for i in range(3001):
        if a[0] <= i <= b[0]:
            dp[0][i] = 1
        if i != 0:
            dp[0][i] += dp[0][i-1]
            dp[0][i] %= MOD
    
    def print_dp(a):
        for i in range(n):
            print(a[i])
    
    #print_dp(dp)
    #print_dp(dp_sum)
    #print(dp[0])
    
    for i in range(1, n):
        for j in range(3001):
            if a[i] <= j <= b[i]:
                dp[i][j] += dp[i-1][j]
                dp[i][j] %= MOD
            if j > 0:
                dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    #print_dp(dp)2
    #print_dp(dp_sum)
    
    print(dp[n-1][b[-1]])

if __name__ == '__main__':
    main()