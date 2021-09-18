import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    t = input()[:-1]
    n = len(s)
    atcoder = "atcoder"
    for i in range(n):
        if s[i] == t[i]:continue
        if s[i] == "@" and t[i] in atcoder:continue
        if t[i] == "@" and s[i] in atcoder:continue
        print("You will lose")
        break
    else:
        print("You can win")
if __name__ == '__main__':
    main()