import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] = max(0, a[i]-10)
    print(sum(a))

if __name__ == '__main__':
    main()