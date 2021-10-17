import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)

    ans = 0
    for i in range(1 << n):
        a = []
        b = []
        for j in range(n):
            if i >> j & 1:
                a.append(s[j])
            else:
                b.append(s[j])
        if len(a) == 0 or len(b) == 0:continue
        a.sort(reverse=True)
        b.sort(reverse=True)
        a = int("".join(a))
        b = int("".join(b))
        ans = max(ans, a*b)
    print(ans)


if __name__ == '__main__':
    main()