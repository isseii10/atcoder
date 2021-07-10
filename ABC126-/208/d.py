import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    edges = [[]*n for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = c
        edges[a].append((b, c))
    
    for i in range(n):
        dist[i][i] = 0

    ans = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
                if dist[i][j] < INF:
                    ans += dist[i][j]
    
    print(ans)
    
    
if __name__ == '__main__':
    main()