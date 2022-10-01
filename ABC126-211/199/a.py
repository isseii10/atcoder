import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    a, b, c = map(int, input().split())
    if a**2 + b**2 < c**2:
        print("Yes")
    else:
        print("No")
        
if __name__ == '__main__':
    main()