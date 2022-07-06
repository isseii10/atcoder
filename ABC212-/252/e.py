import sys
import heapq
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    edges = dict()
    for i in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges[(a, b, c)] = i+1
        G[a].append((c, b))
        G[b].append((c, a))
    
    G_rev = [[-1, -1]]*n
    dist = [INF]*n
    
    q = [[0, 0]]
    dist[0] = 0
    while q:
        c, parent = heapq.heappop(q)
        if c > dist[parent]:continue
        for cost, child in G[parent]:
            if dist[child] <= dist[parent] + cost:continue
            G_rev[child] = [cost, parent]
            dist[child] = dist[parent] + cost
            heapq.heappush(q, [dist[child], child])
    # print(*G_rev)
    ans = []
    for x in range(1, n):
        c, y = G_rev[x]
        if (x, y, c) in edges.keys():
            ans.append(edges[(x, y, c)])
        elif (y, x, c) in edges.keys():
            ans.append(edges[(y, x, c)])
    print(*ans)

if __name__ == '__main__':
    main()