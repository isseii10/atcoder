import sys
from heapq import heappush, heappop, heapify
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353



def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n)]
    total = 0
    edges = defaultdict(int)
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
        total += c
        edges[c] += 1
    

    # G[v] = [w, ...]
    #     グラフG上で頂点vが隣接する辺集合


    used = [0]*n
    que = [(c, w) for w, c in G[0]]
    used[0] = 1
    heapify(que)

    ans = 0
    while que:
        cv, v = heappop(que)
        if used[v]:
                continue
        ans += cv
        edges[cv] -= 1
        used[v] = 1
        for w, c in G[v]:
            if used[w]:
                continue
            heappush(que, (c, w))

    # ansが最小全域木の解
    #print(ans)
    #print(total-ans)
    for c, num in edges.items():
        if c < 0:
            ans += c*num
    print(total-ans)
    

if __name__ == '__main__':
    main()