import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    k = 0
    while 2**k <= n:
        k += 1
    print(max(0, k-1))
if __name__ == '__main__':
    main()