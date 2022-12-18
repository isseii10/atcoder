import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n, a, x, y = map(int, input().split())
    if n <= a:
        print(x*n)
    else:
        print(x*a+y*(n-a))
if __name__ == '__main__':
    main()