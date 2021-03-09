import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    N = int(input())
    

    ans = 0
    for i in range(1, N):
        ans += N / (N-i)
    print("{:.10f}".format(ans))

    

if __name__ == '__main__':
    main()