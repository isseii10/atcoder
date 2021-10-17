import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for sc in a:
        if sc < p:
            ans += 1
    print(ans)
if __name__ == '__main__':
    main()