import sys
from heapq import heappush, heappop

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n+1)]
    r_edges = [[] for _ in range(n+1)]
    in_dig = [0] * (n+1) #入次数
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        r_edges[b].append(a)
        in_dig[b] += 1
    
    fronts = []
    used = set()
    for i in range(1, n+1):
        if in_dig[i] == 0:
            heappush(fronts, i)
    
    ans = []
    while fronts:
        p = heappop(fronts)
        used.add(p)
        ans.append(p)
        for c in edges[p]:
            #cがfrontになりえるか?
            in_dig[c] -= 1
            if in_dig[c] == 0:
                heappush(fronts, c)

    if len(ans) != n:
        print(-1)
    else:
        print(*ans)

    


if __name__ == '__main__':
    main()