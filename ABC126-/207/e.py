import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    

    sum_a = [0]*n
    sum_a[0] = a[0]
    for i in range(1, n):
        sum_a[i] = sum_a[i-1] + a[i]

    dp = [[0]*(n+1) for _ in range(n+1)]
    #dp[i][j] := i番目までの数字を用いてj個に切り分けた時の条件にあう場合の数

    for i in range(n):
        num = a[i]
        for j in range(i+1):
            dp[i+1][j] = dp[i][j]

if __name__ == '__main__':
    main()