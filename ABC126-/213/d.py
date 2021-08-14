import sys
import heapq

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
        heapq.heappush(edges[a], b)
        heapq.heappush(edges[b], a)
    
    visited = [False]*n
    ans = []
    def dfs(p, pp):
        while edges[p]:
            if visited[edges[p][0]]:
                heapq.heappop(edges[p])
            else:
                c = heapq.heappop(edges[p])
                visited[c] = True
                ans.append(c+1)
                dfs(c, p)
                ans.append(p+1)
                dfs(p, pp)

    visited[0] = True
    ans.append(1)
    dfs(0, -1)
    print(*ans)
    
if __name__ == '__main__':
    main()