import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a == 0 and b > 0:
        print("Silver")
    else:
        print("Gold")
if __name__ == '__main__':
    main()