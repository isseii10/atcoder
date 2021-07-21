import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    s = input()[:-1]
    for i in range(n):
        if s[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break
if __name__ == '__main__':
    main()