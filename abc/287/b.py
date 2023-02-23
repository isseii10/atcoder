import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    s = [input()[:-1] for _ in range(n)]
    t = [input()[:-1] for _ in range(m)]
    ans = 0
    for i in range(n):
        ss = s[i][3:]
        for j in range(m):
            if t[j] == ss:
                ans += 1
                break
    print(ans)
if __name__ == '__main__':
    main()