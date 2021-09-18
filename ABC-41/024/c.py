import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, d, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(d)]
    st = [list(map(int, input().split())) for _ in range(k)]

    for i in range(k):
        s, t = st[i]
        days = 0
        for j in range(d):
            days += 1
            l, r = lr[j]
            if l <= s <= r:
                if l <= t <= r:
                    break
                elif t < l:
                    s = l
                else:
                    s = r
        print(days)
if __name__ == '__main__':
    main()