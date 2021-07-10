import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b, c, d = map(int, input().split())
    if c*d - b <= 0:
        print(-1)
    else:
        ans = a // (c*d-b)
        #print(ans)
        if a % (c*d-b) != 0:
            ans += 1
        print(ans)

if __name__ == '__main__':
    main()