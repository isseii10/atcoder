import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dp = [[False]*2 for _ in range(n)]
    dp[0][0] = True
    dp[0][1] = True
    for i in range(n-1):
        if dp[i][0] == True:
            if abs(a[i+1]-a[i]) <= k:
                dp[i+1][0] = True
            if abs(b[i+1]-a[i]) <= k:
                dp[i+1][1] = True
        if dp[i][1] == True:
            if abs(a[i+1]-b[i]) <= k:
                dp[i+1][0] = True
            if abs(b[i+1]-b[i]) <= k:
                dp[i+1][1] = True
    if dp[n-1][0] or dp[n-1][1]:
        print("Yes")
    else:
        print("No")
            
if __name__ == '__main__':
    main()