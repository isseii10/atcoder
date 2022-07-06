from bisect import bisect_left
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    ans = INF
    for i in range(n):
        tgt = a[i]
        idx = bisect_left(b, tgt)
        if idx == 0:
            ans = min(ans, abs(tgt - b[idx]))
        elif idx == m:
            ans = min(ans, abs(tgt - b[idx-1]))
        else:
            ans = min(ans, abs(tgt-b[idx]), abs(tgt-b[idx-1]))
    
    print(ans)

if __name__ == '__main__':
    main()