import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
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
    
    
    ans = 0
    for s in range(n):
        visited = [0]*n
        visited[s] = 1
        q = deque([s])
        while q:
            p = q.pop()
            for c in edges[p]:
                if visited[c]==1:
                    continue
                visited[c] = 1
                q.append(c)
        
        ans += sum(visited)
    
    print(ans)

    

if __name__ == '__main__':
    main()