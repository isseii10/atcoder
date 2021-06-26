import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [list(map(int, input().split())) for _ in range(k)]
    ans = 0
    for i in range(1<<k):
        sara = [0]*n
        for j in range(k):
            c, d = cd[j]
            c -= 1
            d -= 1
            if i >> j & 1:
                sara[c] += 1
            else:
                sara[d] += 1
        
        res = 0
        for a, b in ab:
            a -= 1
            b -= 1
            if sara[a] > 0 and sara[b] > 0:
                res += 1
        ans = max(res, ans)
    print(ans)

if __name__ == '__main__':
    main()