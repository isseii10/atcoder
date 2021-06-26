import sys
from collections import Counter
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    color = list(map(int, input().split()))
    G = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    
    good = [[] for _ in range(n)]
    good[0].append(color[0])
    seen = [-1]*n
    seen[0] = 1
    d = deque()
    d.append(0)
    ans = []
    ans.append(0)
    while d:
        p = d.pop()
        for c in G[p]:
            if seen[c] == 1:
                continue
            seen[c] = 1
            good[c] = good[p]
            good[c].append(color[c])
            if set(good[c]) == len(good[c]):
                ans.append(c)
    
    print(ans)





if __name__ == '__main__':
    main()