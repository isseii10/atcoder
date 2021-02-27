import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    h = list(map(int, input().split()))

    #配るDP
    dp = [INF]*n
    dp[0] = 0
    for i in range(n):
        if i+2 < n:
            dp[i+2] = min(dp[i+2], dp[i] + abs(h[i+2] - h[i]))
        if i+1 < n:
            dp[i+1] = min(dp[i+1], dp[i] + abs(h[i+1] - h[i]))
    print(dp[n-1])


if __name__ == '__main__':
    main()