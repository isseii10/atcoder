import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [INF]*n
    dp[0] = 0
    for i in range(n):
        if i-1 >= 0:
            dp[i] = min(dp[i], dp[i-1]+abs(a[i]-a[i-1]))
        if i-2 >= 0:
            dp[i] = min(dp[i], dp[i-2]+abs(a[i]-a[i-2]))
    print(dp[n-1])
        
if __name__ == '__main__':
    main()