import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, a, b = map(int, input().split())
    total = n*(n+1)//2
    max_a = (n // a) * a
    total_a = (n // a) * (a+max_a) // 2
    max_b = (n // b) * b
    total_b = (n // b) * (b+max_b) // 2
    lcm = (a*b // math.gcd(a, b))
    max_ab = (n // lcm) * lcm
    total_ab = (n // lcm) * (lcm + max_ab) // 2
    print(total - (total_a+total_b-total_ab))
if __name__ == '__main__':
    main()