from ast import iter_child_nodes
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, T = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()

    dp = [[0]*(T) for _ in range(n+1)]
    #dp[i][t]はi番目の料理まででt秒以内に完食している時の満足度の最大値

    for i in range(n):
        a, b = ab[i]
        for t in range(T):
            #食べる
            if t+a < T:
                dp[i+1][t+a] = max(dp[i+1][t+a], dp[i][t] + b)
            #食べない
            dp[i+1][t] = max(dp[i+1][t], dp[i][t])
    
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][T-1] + ab[i][1])
    print(ans)
if __name__ == '__main__':
    main()