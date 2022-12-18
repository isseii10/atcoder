import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    idx = 0
    ans = 0
    while x > 0:
        bit = x % 2
        ans += a[idx]*bit
        x //= 2
        idx += 1
    print(ans)


    
if __name__ == '__main__':
    main()