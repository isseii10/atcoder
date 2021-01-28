import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    import heapq
    n = int(input())
    a = list(map(int, input().split()))
    dp1 = [0]*(n+1)
    former = [a[i] for i in range(n)]
    sum_former = sum(former)
    dp1[0] = sum_former
    heapq.heapify(former)
    for i in range(n):
        x = heapq.heappop(former)
        if a[n+i] > x:
            heapq.heappush(former, a[n+i])
            sum_former += a[n+i] - x
        else:
            heapq.heappush(former, x)
        dp1[i+1] = sum_former

    dp2 = [0]*(n+1)
    latter = [-a[2*n+i] for i in range(n)]
    sum_latter = sum(latter)
    dp2[n] = sum_latter
    heapq.heapify(latter)
    for i in range(n):
        x = heapq.heappop(latter)
        if -a[2*n-1-i] < x:
            heapq.heappush(latter, x)
        else:
            heapq.heappush(latter, -a[2*n-1-i])
            sum_latter += -a[2*n-1-i] - x
        dp2[n-1-i] = sum_latter

    ans = -INF
    for i in range(n+1):
        ans = max(ans, dp1[i]+dp2[i])
    print(ans)



if __name__ == '__main__':
    main()