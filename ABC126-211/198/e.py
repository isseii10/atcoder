from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    C = list(map(int, input().split()))

    edges = [[]*n for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append(b)
        edges[b].append(a)

    used_color = defaultdict(int)
    ans = [0]
    used_color[C[0]] = 1
    def dfs(p, pp):
        for c in edges[p]:
            if c == pp:continue
            if used_color[C[c]] == 0:
                ans.append(c)
            used_color[C[c]] += 1
            dfs(c, p)
            used_color[C[c]] -= 1
    
    dfs(0, -1)
    ans.sort()
    for a in ans:
        print(a+1)




    
if __name__ == '__main__':
    main()