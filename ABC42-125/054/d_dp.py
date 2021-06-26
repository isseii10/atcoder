import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n, ma, mb = map(int, input().split())
    abc = [list(map(int, input().split())) for _ in range(n)]

    #dp[i][wa][wb] := i番目までみて、aの重さがwa、bの重さがwbの時の最小コスト
    dp = [[[INF]*410 for _ in range(410)] for _ in range(n+1)]
    dp[0][0][0] = 0

    for i in range(n):
        a, b, c = abc[i]
        for wa in range(400):
            for wb in range(400):
                dp[i+1][wa+a][wb+b] = min(dp[i+1][wa+a][wb+b], dp[i][wa][wb] + c)
                dp[i+1][wa][wb] = min(dp[i+1][wa][wb], dp[i][wa][wb])

    ans = INF
    for wa in range(400):
        for wb in range(400):
            if dp[n][wa][wb] != 0 and wa*mb == wb*ma:
                ans = min(ans, dp[n][wa][wb])
    
    if ans == INF:ans = -1
    print(ans)
    
if __name__ == '__main__':
    main()