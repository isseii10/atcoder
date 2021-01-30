import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353



def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    k = int(input())
    cs = list(map(int, input().split()))
    
    dist_c = [[INF]*k for _ in range(k)]

    
    def BFS(start):
        q = deque()
        q.append(start)
        dist = [INF]*n
        dist[start] = 0
        while q:
            par = q.popleft()
            for chi in edges[par]:
                if dist[chi] != INF:
                    continue
                dist[chi] = dist[par] + 1
                q.append(chi)
        return dist
    
    # n頂点のグラフをcのみのグラフに変換
    for i in range(k):
        dist_from_ci = BFS(cs[i]-1)
        for j in range(k):
            dist_c[i][j] = dist_from_ci[cs[j]-1]
            if dist_c[i][j] == INF:
                print(-1)
                exit()
    dp = [[INF]*k for _ in range(1<<k)]

    #どこからスタートしても良いので、初期化は各ビットが立っているとこに１
    for i in range(k):
        dp[1<<i][i] = 1

    #bitDP
    for i in range(1<<k):
        for now in range(k):
            if (i >> now & 1) == 0:continue
            for nxt in range(k):
                if (i >> nxt) & 1:continue
                dp[i^(1<<nxt)][nxt] = min(dp[i^(1<<nxt)][nxt], dp[i][now]+dist_c[now][nxt])
    #print(dp)
    ans = INF
    for i in range(k):
        ans = min(ans, dp[(1<<k)-1][i])
    print(ans)
if __name__ == '__main__':
    main()