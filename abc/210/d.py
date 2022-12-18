import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def solve(A, h, w, c):
    dp = [[INF]*(w) for _ in range(h)]
    #dp[i][j] := (i,j)よりも左上{(i, j)を含む}の領域の点(i', j')のA[i'][j']-C*(i'+j')の最小値
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:dp[i][j] = A[i][j] - c*(i+j)
            elif i == 0 and j != 0:
                dp[i][j] = min(dp[i][j-1], A[i][j] - c*(i+j))
            elif i != 0 and j == 0:
                dp[i][j] = min(dp[i-1][j], A[i][j]-c*(i+j))
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], A[i][j]-c*(i+j))
            
    ans = INF
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:continue
            elif i == 0 and j != 0:
                ans = min(ans, dp[i][j-1] + A[i][j] + c*(i+j))
            elif i != 0 and j == 0:
                ans = min(ans, dp[i-1][j] + A[i][j]+ c*(i+j))
            else:
                ans = min(ans, dp[i-1][j]+A[i][j]+c*(i+j), dp[i][j-1]+A[i][j]+c*(i+j))

    return ans


def main():
    h, w, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]

    #右下に移動する鉄道を考える(左下はグリッドを反転すれば良い)
    #右下なので、絶対値が外れて、　C*(i-i')+C*(j-j') = C*(i+j)-C*(i'+j')
    #と二点で分けて考えられる
    A_r = [A[i][::-1] for i in range(h)]

    ans1 = solve(A, h, w, c)
    ans2 = solve(A_r, h, w, c)
    print(min(ans1, ans2))





if __name__ == '__main__':
    main()