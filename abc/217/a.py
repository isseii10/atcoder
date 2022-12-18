import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s, t = input()[:-1].split()
    if s < t:
        print("Yes")
    else:
        print("No")
if __name__ == '__main__':
    main()