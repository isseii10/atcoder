import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    q = int(input())
    s = []
    s_rev = []
    s_count = defaultdict(int)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            heapq.heappush(s, x)
            heapq.heappush(s_rev, -x)
            s_count[x] += 1
        elif query[0] == 2:
            x, c = query[1:]
            s_count[x] = max(0, s_count[x]-c)
        else:
            while s_count[s[0]] == 0:
                heapq.heappop(s)
            while s_count[-s_rev[0]] == 0:
                heapq.heappop(s_rev)
            print(-s_rev[0] - s[0])

if __name__ == '__main__':
    main()