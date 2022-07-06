import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    d_count = defaultdict(int)
    for i in range(k):
        d_count[c[i]] += 1
    
    res = len(d_count.keys())
    ans = len(d_count.keys())
    for i in range(1, n-k+1):
        delta = 0
        left = c[i-1]
        d_count[left] -= 1
        if d_count[left] == 0:
            delta -= 1

        new = c[i+k-1]
        if d_count[new] == 0:
            delta += 1
        d_count[new] += 1

        res = res + delta
        ans = max(ans, res)
    
    print(ans)


if __name__ == '__main__':
    main()