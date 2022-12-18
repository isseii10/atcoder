import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    aoki_score = [[0]*n for _ in range(n)]
    takahashi_score = [[0]*n for _ in range(n)]
    for l in range(n):
        for r in range(n):
            for flag, i in enumerate(range(l, r+1)):
                if flag % 2 == 0:
                    takahashi_score[l][r] += A[i]
                else:
                    aoki_score[l][r] += A[i]
            



if __name__ == '__main__':
    main()