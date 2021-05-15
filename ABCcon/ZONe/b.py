import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, D, H = map(int, input().split())
    max_obj = [0, 0] #d h
    ans = 0.0
    for _ in range(n):
        d, h = map(int, input().split())
        ans = max(ans, (D*h - H*d) / (D-d))
    print(max(0.0, ans))

if __name__ == '__main__':
    main()