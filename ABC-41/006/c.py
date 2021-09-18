import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    if m - 2*n < 0:
        print(-1, -1, -1)
        exit()
    for z in range((m-2*n) // 2 + 1):
        y = m - 2*n - 2*z
        x = n - y - z
        if y < 0 or x < 0:continue
        print(x, y, z)
        break
    else:
        print(-1, -1, -1)
if __name__ == '__main__':
    main()