import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int,input().split())
    time = [[INF]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        time[a][b] = c
        time[b][a] = c
    
    for i in range(n):
        time[i][i] = 0
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                time[i][j] = min(time[i][j], time[i][k]+time[k][j])
    
    min_time = INF
    for i in range(n):
        min_time = min(min_time, max(time[i]))
    print(min_time)

if __name__ == '__main__':
    main()