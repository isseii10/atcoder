import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b, c, d, e = map(int, input().split())
    ans = []
    for x, y, z in combinations([a, b, c, d, e], 3):
        ans.append(x+y+z)
    ans.sort()
    print(ans[-3])
if __name__ == '__main__':
    main()