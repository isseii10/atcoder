import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(input().split()))
    b = [0]*m
    AnBm = [[0]*m for _ in range(n)]
    b[m] = c[m+n] // a[n]
    AnBm[n][m] = c[n+m]
        
        

if __name__ == '__main__':
    main()