import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, x = map(int, input().split())
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    for c in alp:
        res += c*n
    print(res[x-1])

if __name__ == '__main__':
    main()