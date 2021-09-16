import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    sum_h = [0]*h
    sum_w = [0]*w
    for i in range(h):
        for j in range(w):
            sum_h[i] += a[i][j]
            sum_w[j] += a[i][j]
    
    b = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            b[i][j] = sum_h[i] + sum_w[j] - a[i][j]
    
    for i in range(h):
        print(*b[i])
if __name__ == '__main__':
    main()