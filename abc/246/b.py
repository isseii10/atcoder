import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(float, input().split())
    sin2 = b*b / (a*a + b*b)
    cos2 = a*a / (a*a + b*b)
    print(cos2**0.5, sin2**0.5)
if __name__ == '__main__':
    main()