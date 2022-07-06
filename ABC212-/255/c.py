import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x, a, d, n = map(int, input().split())
    if d >= 0:
        x -= a
        if x <= 0 or d*(n-1) < x:
            print(min(abs(x), abs(x-d*(n-1))))
        else:
            pos = x % d
            print(min(pos, d-pos))
    else:
        x -= a + d*(n-1)
        d = -d
        if x <= 0 or d*(n-1) < x:
            print(min(abs(x), abs(x-d*(n-1))))
        else:
            pos = x % d
            print(min(pos, d-pos))


    
if __name__ == '__main__':
    main()