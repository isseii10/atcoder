import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def main():
    t = int(input())
    for _ in range(t):
        L, R = map(int, input().split())
        # a-2*L+1
        n = R-2*L+1
        if n < 0:
            ans = 0
        else:
            ans = n*(1+R-2*L+1)//2
        print(ans)


if __name__ == '__main__':
    main()