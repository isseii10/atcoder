import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    x = input()[:-1]
    alpha_dict = dict()
    for i, a in enumerate(x):
        alpha_dict[a] = chr(i+ord("a"))

    n = int(input())
    s = [input()[:-1] for _ in range(n)]
    s_ = []
    for i in range(n):
        res = ""
        for c in s[i]:
            res += alpha_dict[c]
        s_.append((res, i))

    #print(s_)

    s_.sort()
    for _, i in s_:
        print(s[i])


if __name__ == '__main__':
    main()