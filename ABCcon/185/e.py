#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dp = [[INF]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    # dp[i][j] := i番目とj番目にポインタがいる時のコストの最小値


    #下のコメントアウトがなぜだめかというと、
    # ポインタiがnまできた時にまだポインタjがmまできてない時の操作ができていないから
    """
    for i in range(n):
        for j in range(m):
            c = 0
            if a[i] != b[j]:
                c = 1
            dp[i+1][j+1] = min(min(dp[i][j+1]+1, dp[i+1][j]+1), dp[i][j]+c)
    """
    for i in range(n+1):
        for j in range(m+1):
            #ポインタiがn未満の時は、ポインタiをインクリメントする操作ができる
            #jの位置に依らない
            if i < n: dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            #ポインタjがm未満の時は、ポインタjをインクリメントする操作ができる
            #iの位置に依らない
            if j < m: dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            #ポインタが両方インクリメントできる場合は、両方動かす操作ができる
            if i < n and j < m:
                c = 1
                if a[i]==b[j]: c = 0
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j] + c)


    #for i in range(n+1):
    #    print(dp[i])
    print(dp[n][m])

if __name__ == '__main__':
    main()