import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1
    edges = [[]*n for _ in range(n)]
    for _ in range(m):
        a, b, t, k = map(int, input().split())
        a -= 1 
        b -= 1
        edges[a].append([b, t, k])
        edges[b].append([a, t, k])
    
    hq = []
    heapq.heappush(hq, [0, x])
    dist = [INF]*n
    dist[x] = 0
    while hq:
        now, p = heapq.heappop(hq)
        #----------------------------------------
        #この一行大事！！！
        if dist[p] < now:continue
        #----------------------------------------
        for c, t, k in edges[p]:
            #dist[c]は到着時刻にしたい
            if dist[c] <= dist[p] + (k- dist[p]%k)%k + t:continue
            dist[c] = dist[p] + (k- dist[p]%k)%k + t
            heapq.heappush(hq, [dist[c], c])

    if dist[y] != INF:
        print(dist[y])
    else:
        print(-1) 

if __name__ == '__main__':
    main()