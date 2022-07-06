#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

def main():
    n = int(input())
    pos = []
    for i in range(n):
        x, y, z = map(int, input().split())
        pos.append((x, y, z))
    
    G = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x1, y1, z1 = pos[i]
            x2, y2, z2 = pos[j]
            G[i][j] = abs(x2-x1)+abs(y2-y1)+max(0, z2-z1)
    
    start = 0
    dp = [[INF]*(n) for _ in range(1<<(n))]
    #dp[i][j] := iの状態（bitで通ってきた街を管理する） で次に街jに移動する時のコストの最小値
    dp[0][0] = 0

    for i in range(1<<n):
        for j in range(n):
            for k in range(n):
                if ((i >> j) & 1) == 0:
                    dp[i ^ (1<<j)][k] = min(dp[i^(1<<j)][k], dp[i][j]+G[j][k])


    #for i in range(n):
    #    print(G[i])
    #print("------------")
    #for i in range(1<<n):
    #    print(dp[i])

    ans = INF
    for j in range(n):
        ans = min(ans, dp[(1<<n)-1][j] + G[j][0])
    print(ans) 

if __name__ == '__main__':
    main()