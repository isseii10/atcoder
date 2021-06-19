import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    n *= 1.08
    if int(n) < 206:
        print('Yay!')
    elif int(n) == 206:
        print('so-so')
    else:
        print(':(')
if __name__ == '__main__':
    main()