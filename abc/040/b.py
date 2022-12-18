import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ans = INF
    for h in range(1, n+1):
        w = n // h
        amari = n % h
        #print(h, w, amari)
        ans = min(ans, abs(h-w)+amari)
    print(ans)
if __name__ == '__main__':
    main()