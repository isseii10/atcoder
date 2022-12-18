import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    x = int(input())
    a = x % 100
    print(100 - a)

if __name__ == '__main__':
    main()