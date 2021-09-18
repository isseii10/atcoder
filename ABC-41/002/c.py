import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
    x_a -= x_c
    y_a -= y_c
    x_b -= x_c
    y_b -= y_c
    print(abs(x_b*y_a - y_b*x_a) / 2)
if __name__ == '__main__':
    main()