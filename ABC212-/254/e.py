import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    G = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    used = set()
    def dfs(p, d):
        used.add(p)
        if d == 0:return
        for c in G[p]:
            dfs(c, d-1)

    q = int(input())
    for _ in range(q):
        x, k = map(int, input().split())
        used = set()
        dfs(x, k)
        print(sum(used))





if __name__ == '__main__':
    main()