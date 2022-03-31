import sys
from collections import defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    ans = (n * (n-1) * (n-2)) // (3*2)
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                x3, y3 = xy[k]
                if (x2-x1) * (y3-y2) == (x3-x2) * (y2-y1):
                    ans -= 1
    print(ans)



if __name__ == '__main__':
    main()