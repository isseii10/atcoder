import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    ans = s.count('ZONe')
    print(ans)

if __name__ == '__main__':
    main()