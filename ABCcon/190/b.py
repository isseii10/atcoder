import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for x, y in xy:
        if x < s and y > d:
            print("Yes")
            exit()
    print("No")
if __name__ == '__main__':
    main()