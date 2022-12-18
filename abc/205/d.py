import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))

    for _ in range(q):
        k = int(input())
        idx1 = bisect_right(a, k)
        if idx1 == 0 or idx1 == n:
            print(k+idx1)
        else:
            idx2 = bisect_right(a, k+idx1)
            while idx1 != idx2:
                idx1 = idx2
                idx2 = bisect_right(a, k+idx2)
            print(idx2+k)


        

if __name__ == '__main__':
    main()