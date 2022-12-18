import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    mt = []
    for _ in range(n):
        s, t = input().split()
        t = int(t)
        mt.append([t, s])
    mt.sort()
    print(mt[-2][1])
if __name__ == '__main__':
    main()