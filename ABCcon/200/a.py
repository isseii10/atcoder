import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    cent = 1
    cent_100 = 100
    while cent_100 < n:
        cent_100 += 100
        cent += 1
    print(cent)
if __name__ == '__main__':
    main()