import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))

    dp0 = [[INF]*2 for _ in range(n+1)] # dp0は0番目にA[0]で餌をあげた場合
    dp1 = [[INF]*2 for _ in range(n+1)] # dp1は0番目にA[-1]で餌をあげた場合
    # dp[i][0]
    # dp[i][1] はi+1にもあげている状態
    dp0[0][0] = 0
    dp0[0][1] = INF
    
    for i in range(1, n):
        # A[i]で餌をあげる場合 
        dp0[i][1] = min(dp0[i-1][0], dp0[i-1][1]) + A[i]
        # a[i]で餌をあげない場合
        dp0[i][0] = dp0[i-1][1]
        
    dp1[0][0] = INF
    dp1[0][1] = A[-1]

    for i in range(n):
        # A[i]で餌をあげる場合 
        dp0[i+1][1] = min(dp0[i][0], dp0[i][1]) + A[i]
        # a[i]で餌をあげない場合
        dp0[i+1][0] = dp0[i][1]
    print(min(dp0[n-1][0]))
if __name__ == '__main__':
    main()