import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0]*10 for _ in range(n)]
    dp[0][a[0]] = 1
    for i in range(n-1):
        right = a[i+1]
        for left in range(10):
            #F
            dp[i+1][(left+right)%10] += dp[i][left]
            dp[i+1][(left+right)%10] %= MOD
            #G
            dp[i+1][(left*right)%10] += dp[i][left]
            dp[i+1][(left*right)%10] %= MOD
    
    for i in range(10):
        print(dp[n-1][i])



if __name__ == '__main__':
    main()