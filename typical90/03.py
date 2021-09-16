from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    edges = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)


    def dfs(p, depth):
        for c in edges[p]:
            if depth[c] != -1:continue
            depth[c] = depth[p] + 1
            dfs(c, depth)

    #まず適当にdfsして深さ最大の葉(start)を見つける
    depth = [-1]*n
    depth[0] = 1
    dfs(0, depth)
    max_depth = max(depth)
    start = -1
    for i in range(n):
        if depth[i] == max_depth:
            start = i
            break
    
    #startから再度dfsして最大のパスを見つける
    new_depth = [-1]*n
    new_depth[start] = 1
    dfs(start, new_depth)
    print(max(new_depth))
    

if __name__ == '__main__':
    main()