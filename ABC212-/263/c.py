import sys
from itertools import combinations, product
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    d = range(1, m+1)
    tmp = combinations(d, n)
    for t in tmp:
        print(*t)

if __name__ == '__main__':
    main()