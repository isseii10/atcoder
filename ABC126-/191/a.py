import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    v, t, s, d = map(int, input().split())
    if v*t <= d <= v*s:
        print("No")
    else:
        print("Yes")
if __name__ == '__main__':
    main()