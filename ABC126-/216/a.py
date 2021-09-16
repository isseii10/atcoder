import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x, y = input()[:-1].split(".")
    y = int(y)
    if y <= 2:
        print(x+"-")
    elif y <= 6:
        print(x)
    else:
        print(x+"+")
if __name__ == '__main__':
    main()