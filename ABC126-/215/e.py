import sys
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
#MOD = 10**9+7
MOD = 998244353


def main():
    n = int(input())
    s = input()[:-1]
    # A ~ J 10個
    dp = [[0]*(n+1) for _ in range(10)]
    #dp[i][j]はi文字目までで条件を満たすコンテストへの出方で最後のアルファベットがjの場合の数
    dp[0] = 1 #から文字
    used = [[set() for _ in range(n)] for _ in range(10)]
    #nxt[c][i] := i文字目以降でcが始めて登場するインデックス
    nxt = [[n]*(n+1) for _ in range(10)]
    for i in range(n)[::-1]:
        for j in range(10):
            nxt[j][i] = nxt[j][i+1]
        nxt[ord(s[i])-ord("A")][i] = i
    print(nxt)

    for i in range(n):
        c = s[i]
        for j in range(10):
            if nxt[j][i] >= n:continue
            if c not in used[i][j]:
                dp[nxt[j][i]+1][ord(c)-ord("A")] += dp[i][j]
                dp[nxt[j][i]+1][ord(c)-ord("A")] %= MOD
                used[nxt[j][i]+1][ord(c)-ord("A")] = used[i][j]
                if ord(c) - ord("A") != j:
                    used[nxt[j][i]+1][ord(c)-ord("A")].add(j)
    ans = 0
    for i in range(10):
        ans += dp[n][i]
        ans %= MOD
    print(ans)
            

    


if __name__ == '__main__':
    main()