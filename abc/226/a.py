import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x = input()[:-1]
    a, b = x.split(".")
    ans = int(a)
    if int(b[0]) < 5:
        pass
    else:
        ans += 1
    print(ans)
if __name__ == '__main__':
    main()