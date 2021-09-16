import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)
if __name__ == '__main__':
    main()