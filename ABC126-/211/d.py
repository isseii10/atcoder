import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    edges = [[]*n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    
    dp = [INF]*n
    dp[0] = 0
    #dp[i]は都市1から都市iまでの最短経路長
    num = [0]*n
    num[0] = 1
    #num[i]は都市1から都市iまでの最短経路の場合の数

    q = deque()
    q.append(0)
    while q:
        p = q.popleft()
        for c in edges[p]:
            if dp[c] > dp[p] + 1:
                dp[c] = dp[p] + 1
                num[c] = num[p]
                q.append(c)
            elif dp[c] == dp[p] + 1:
                num[c] = (num[c] + num[p]) % MOD
    
    #print(dp[n-1])
    print(num[n-1])
            

if __name__ == '__main__':
    main()