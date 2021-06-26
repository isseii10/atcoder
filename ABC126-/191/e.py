import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    G = [[INF]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a][b] = min(G[a][b], c)
    #隣接リストに直す
    edge = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != INF:
                edge[i].append((j, G[i][j]))
    
    for i in range(n):
        time = [INF]*n
        time[i] = 0
        q = []
        heappush(q, (time[i], i))
        while q:
            p_cost, p = heappop(q)
            if time[p] < p_cost:continue
            for c, cost in edge[p]:
                if c == i and time[i]==0:
                    time[c] = p_cost + cost
                if time[c] <= p_cost + cost:continue
                time[c] = p_cost + cost
                heappush(q, (time[c], c))

        if time[i] == 0:
            time[i] = -1
        print(time[i])

if __name__ == '__main__':
    main()