import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    left = A[0]
    right = B[0]
    for i in range(n):
        if left < A[i]:
            left = A[i]
        if B[i] < right:
            right = B[i]
    print(max(0, right-left+1))

if __name__ == '__main__':
    main()