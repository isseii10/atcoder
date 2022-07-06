from sys import setrecursionlimit
from typing import Deque
setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
inf = float('inf')

def dfs(p, pp, G, depth):
    for c in G[p]:
        if c == pp: continue
        depth[c] = depth[p] + 1
        dfs(c, p, G, depth)


def main():
    n = int(input())
    edge_list = [[]*n for _ in range(n)]
    edges = []
    c = [0]*n
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge_list[a].append(b)
        edge_list[b].append(a)
        edges.append((a, b))

    root = 0
    depth = [-1]*n
    dfs(0, -1, edge_list, depth)
    #print(depth)

    q = int(input())
    c = [0]*n
    for _ in range(q):
        t, e, x = map(int, input().split())
        a, b = edges[e-1]
        if t == 1:
            if depth[a] < depth[b]:
                c[0] += x
                c[b] -= x
            else:
                c[a] += x
        else:
            if depth[a] < depth[b]:
                c[b] += x
            else:
                c[0] += x
                c[a] -= x

    #print(c)
    #最後に累積和を木上でとる
    from collections import deque
    q = deque()
    q.append(0)
    visited = [False]*n
    visited[0] = True
    while q:
        p = q.popleft()
        for child in edge_list[p]:
            if visited[child]:continue
            visited[child] = True
            c[child] += c[p]
            q.append(child)

    for i in range(n):
        print(c[i])

if __name__ == '__main__':
    main()