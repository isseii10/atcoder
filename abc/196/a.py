import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(int, input().split())    
    c, d = map(int, input().split())
    ans = -INF
    for x in range(a, b+1):
        for y in range(c, d+1):
            ans = max(ans, x-y)
    print(ans)

if __name__ == '__main__':
    main()