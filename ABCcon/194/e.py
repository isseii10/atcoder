import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    mex = 0
    seen = [False] * 2000000
    for i in range(m):
        seen[A[i]] = True
        while seen[mex]:
            mex += 1

    min_mex = mex
    #print(min_mex)
    for l in range(1, n-m):
        seen[A[l-1]] = False
        if min_mex > A[l-1]:
            min_mex = A[l-1]
        seen[A[l+m]] = True
        while seen[min_mex]:
            min_mex += 1
        print(min_mex)
    #print(min_mex)

    
if __name__ == '__main__':
    main()