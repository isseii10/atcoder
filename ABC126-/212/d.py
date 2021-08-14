import sys
import heapq


input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353



def main():
    q = int(input())
    hq = []
    bias = 0
    for i in range(q):
        query = list(map(int, input().split()))
        p = query[0]
        if p == 1:
            x = query[1]
            heapq.heappush(hq, x - bias)
        elif p == 2:
            x = query[1]
            bias += x
        else:
            ans = heapq.heappop(hq) + bias
            print(ans)


if __name__ == '__main__':
    main()