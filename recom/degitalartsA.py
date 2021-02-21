import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    S = list(input()[:-1].split(" "))
    n = int(input())

    for _ in range(n):
        ng = input()[:-1]
        for j, s in enumerate(S):
            if len(ng) != len(s):continue
            for k, c in enumerate(s):
                if ng[k] == '*':continue
                if ng[k] != c:
                    break
            else:
                S[j] = '*' * len(s)
    print(*S)



if __name__ == '__main__':
    main()