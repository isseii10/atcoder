import sys
from collections import defaultdict

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i-1] += 1
        d[i] += 1
        d[i+1] += 1
    ans = 0
    for v in d.values():
        ans = max(ans, v)
    print(ans)
if __name__ == '__main__':
    main()  