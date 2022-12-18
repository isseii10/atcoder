import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)
    t = ""
    for i in range(n)[::-1]:
        if s[i] == "6":
            t += "9"
        elif s[i] == "9":
            t += "6"
        else:
            t += s[i]
    print(t)


if __name__ == '__main__':
    main()