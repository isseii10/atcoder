import sys
from collections import defaultdict
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a[i] -= 1
    a_set = set(a)
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        if i in a_set:
            continue
        for j in range(k):
            dist[i][a[j]] = (xy[i][1] - xy[a[j]][1]) ** 2 + (xy[i][0] - xy[a[j]][0]) ** 2
    for i in range(n):
        if i in a_set:continue
        ans = max(ans, min(dist[i]))
    print(math.sqrt(ans))
    

    
if __name__ == '__main__':
    main()