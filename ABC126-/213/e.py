import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    s = [input()[:-1] for _ in range(h)]
    move1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    punch_move = []
    dp = [[INF]*(w) for _ in range(h)]
    # dp[i][j] i, jマスに到達するために必要なパンチの回数

    d = deque()
    d.append((0, 0))
    dp[0][0] = 0

    cannot_move = ((-2, -2), (-2, 2), (2, -2), (2, 2))

    while d:
        py, px = d.popleft()
        #move1 bfs
        for dy, dx in move1:
            if 0 <= px+dx < w and 0 <= py+dy < h:
                cy = py + dy
                cx = px + dx
                if s[cy][cx] == "." and dp[cy][cx] > dp[py][px]:
                    dp[cy][cx] = dp[py][px]
                    d.appendleft((cy, cx))
                    # move1のbfsを優先的に探索したいからd.appendleftする
    
        #punch
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                if (dy, dx) in cannot_move:continue 
                if 0 <= px+dx < w and 0 <= py+dy < h:
                    punchx = px + dx
                    punchy = py + dy
                    if s[punchy][punchx] == "#" and dp[punchy][punchx] > dp[py][px]+1:
                        dp[punchy][punchx] = dp[py][px] + 1
                        d.append((punchy, punchx))
    
    
    print(dp[h-1][w-1])
                



if __name__ == '__main__':
    main()