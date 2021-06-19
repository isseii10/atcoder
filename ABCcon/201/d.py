import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    H, W = map(int, input().split())
    A = [input()[:-1] for _ in range(H)]
    dp = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        for j in range(W):
            if (i + j) %2 == 0:
                dp[i][j] = INF
            else:
                dp[i][j] = -INF
    dp[0][0] = 0
    

    q = deque()

    q.append((0, 0))
    while q:
        i, j = q.popleft()
        n = i+j
        if n % 2 == 0:
            #T
            if i+1 < H:
                if A[i+1][j] == '+':
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + 1)
                else:
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] - 1)
                q.append((i+1, j))

            if j+1 < W:
                if A[i][j+1] == '+':
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + 1)
                else:
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] - 1)
                q.append((i, j+1))

        else:
            #A
            if i+1 < H:
                if A[i+1][j] == '+':
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] - 1)
                else:
                    dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
                q.append((i+1, j))
            
            if j+1 < W:
                if A[i][j+1] == '+':
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j] - 1)
                else:
                    dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
                q.append((i, j+1))
            
    print(dp)


    
if __name__ == '__main__':
    main()