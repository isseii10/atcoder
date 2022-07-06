import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, u, v = map(int, input().split())
    u -= 1
    v -= 1
    # u:追われる　v:追う
    # 逃げ→追うの順番

    edges = [[]*n for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)
    
    if u == v:
        print(0)
        exit()

    depth = [-1]*n
    to_leaf = [0]*n
    parent = [0]*n

    def dfs(p):
        for c in edges[p]:
            if depth[c] != -1:continue
            depth[c] = depth[p] + 1
            parent[c] = p
            dfs(c)
            to_leaf[p] = max(to_leaf[p], to_leaf[c] + 1)
    
    depth[v] = 0
    parent[v] = -1
    dfs(v)
    #print(depth)
    #print(to_leaf)

    #yoyu := takahashiがaokiに近づける回数
    yoyu = (depth[u] - 1) // 2
    # between := takahashiがaokiに限界まで近づいた時の位置関係(間にノードがあるかどうか)
    between = (depth[u] - 1) % 2
    p = u
    max_to_leaf = to_leaf[u]
    for i in range(1, yoyu+1):
        p = parent[p]
        max_to_leaf = max(max_to_leaf, i+to_leaf[p])

    
    ans = max_to_leaf + between
    print(ans)
    
if __name__ == '__main__':
    main()