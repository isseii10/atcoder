import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [INF]*n
    dp[0] = 0
    for i in range(n):
        for k in range(1, K+1):
            if i+k < n:
                dp[i+k] = min(dp[i+k], dp[i]+abs(h[i+k]-h[i]))
    print(dp[n-1])
    
if __name__ == '__main__':
    main()