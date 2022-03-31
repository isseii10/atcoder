import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    if s[-1] == "r":
        print("er")
    else:
        print("ist")
if __name__ == '__main__':
    main()