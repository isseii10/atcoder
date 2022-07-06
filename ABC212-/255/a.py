import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(a[r-1][c-1])
if __name__ == '__main__':
    main()