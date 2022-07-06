import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(int, input().split())
    print(32**(abs(a-b)))
if __name__ == '__main__':
    main()