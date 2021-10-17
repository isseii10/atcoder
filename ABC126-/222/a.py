import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = input()[:-1]
    while len(n) < 4:
        n = '0' + n
    print(n)
if __name__ == '__main__':
    main()