import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print('expert')
if __name__ == '__main__':
    main()