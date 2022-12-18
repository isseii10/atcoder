import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    
    magic_set = set()
    for i in range(n-1):
        x1, y1 = xy[i]
        for j in range(i+1, n):
            x2, y2 = xy[j]
            dx, dy = x2-x1, y2-y1
            abs_dx, abs_dy = abs(dx), abs(dy)
            g = math.gcd(abs_dx, abs_dy)
            dx //= g
            dy //= g
            #print(dx, dy)
            magic_set.add((dx, dy))
            magic_set.add((-dx, -dy))
    print(len(magic_set))
    
if __name__ == '__main__':
    main()