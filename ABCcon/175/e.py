#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    R, C, K = map(int, input().split())
    meiro = [[0]*C for _ in range(R)]

    """
    for _ in range(K):
        r, c, v = map(int, input().split())
        r -= 1
        c -= 1
        meiro[r][c] = v
    """
    rcv = [list(map(int, input().split())) for _ in range(K)]
    for i in range(K):
        r, c, v = rcv[i]
        meiro[r-1][c-1] = v

    #本当はdp= [[[0]*C for _ in range(R)] for _ in range(4)]
    #として、dp[i][r][c]としたいところだが、制約的にR＊C＊4のループは厳しい（3000*3000*4 = 3.6*10**7)
    #そこで、iのループをなくすためにそれぞれにdpテーブルを作る
    dp0 = [[0]*C for _ in range(R)]
    dp1 = [[0]*C for _ in range(R)]
    dp2 = [[0]*C for _ in range(R)]
    dp3 = [[0]*C for _ in range(R)]

    dp1[0][0] = meiro[0][0]

    #dp_i[r][c]:=(r, c)にいてr行上のアイテムをi個持っているときの、その価値の総和の最大値
    for r in range(R):
        for c in range(C):
            if r+1 < R:
                dp0[r+1][c] = max(dp0[r+1][c], dp1[r][c], dp2[r][c], dp3[r][c])
                dp1[r+1][c] = max(dp1[r+1][c], dp0[r][c]+meiro[r+1][c], dp1[r][c] + meiro[r+1][c], dp2[r][c]+meiro[r+1][c], dp3[r][c]+meiro[r+1][c])

            if c+1 < C:
                dp0[r][c+1] = max(dp0[r][c+1], dp0[r][c])
                dp1[r][c+1] = max(dp1[r][c+1], dp1[r][c])
                dp2[r][c+1] = max(dp2[r][c+1], dp2[r][c])
                dp3[r][c+1] = max(dp3[r][c+1], dp3[r][c])
                
                dp1[r][c+1] = max(dp1[r][c+1],
                                    dp0[r][c] + meiro[r][c+1])
                dp2[r][c+1] = max(dp2[r][c+1],
                                    dp1[r][c] + meiro[r][c+1])
                dp3[r][c+1] = max(dp3[r][c+1],
                                    dp2[r][c] + meiro[r][c+1])
    print(max(dp0[R-1][C-1], dp1[R-1][C-1], dp2[R-1][C-1], dp3[R-1][C-1]))
if __name__ == '__main__':
    main()