import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    xyp = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x1, y1, p1 = xyp[i]
            x2, y2, p2 = xyp[j]
            d = (abs(x2-x1)+abs(y2-y1))
            if d % p1 == 0:
                dist[i][j] = d // p1
            else:
                dist[i][j] = (d // p1) + 1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] >= dist[i][k] and dist[i][j] >= dist[k][j]:
                    dist[i][j] = max(dist[i][k], dist[k][j])
    ans = INF
    for s in range(n):
        #print("start {} \n dist[{}] = {}".format(s, s, dist[s]))
        ans = min(ans, max(dist[s]))
    print(ans)

if __name__ == '__main__':
    main()