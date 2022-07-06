import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x = int(input())
    if x == 0:
        print("No")
    else:
        if x % 100 == 0:
            print("Yes")
        else:
            print("No")
if __name__ == '__main__':
    main()