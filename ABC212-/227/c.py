import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ans = 0
    # math.pow でaの最大値を求めるよりも、超えたらループ抜けるって方が誤差なくて良い
    for a in range(1, n+1):
        if a*a*a > n:
            break
        bc = n // a
        for b in range(a, n+1):
            if a*b*b > n:
                break
            c = int(bc / b)
            if b <= c:
                ans += c-b+1
    print(ans)
if __name__ == '__main__':
    main()