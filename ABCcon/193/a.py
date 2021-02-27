import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(int, input().split())
    print(100 - (b / a * 100))
if __name__ == '__main__':
    main()