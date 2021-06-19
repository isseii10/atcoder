import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    t = list(map(int, input().split()))
    dp = [0]*(n+1)
    total = sum(t)
    #dp[i]:= i番目までの料理の最小時間


if __name__ == '__main__':
    main()