import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    b = sorted(set(a))
    d = {v:i for i, v in enumerate(b)}
    for ai in a:
        print(d[ai])



if __name__ == '__main__':
    main()