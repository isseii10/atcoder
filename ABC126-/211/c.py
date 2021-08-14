import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    s = input()[:-1]
    n = len(s)
    name = ['c', 'h', 'o', 'k', 'u', 'd', 'a', 'i']
    dp = [[0]*(8) for _ in range(n+1)]
    #dp[i][idx]はi番目までの文字列で、最後の文字がidxであるものの場合の数
    for i in range(n):
        for idx, c in enumerate(name):
            if s[i] != c:
                dp[i+1][idx] = dp[i][idx]
            else:
                dp[i+1][idx] = dp[i][idx]
                if idx > 0:
                    dp[i+1][idx] = (dp[i+1][idx] + dp[i][idx-1]) % MOD
                else:
                    dp[i+1][idx] = dp[i][idx] + 1
    
    #for i in range(n+1):
    #    print(dp[i])
    print(dp[n][7])

if __name__ == '__main__':
    main()