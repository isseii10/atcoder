import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    #print(xy)
    xy_set = set(xy)
    ans = 0
    counted = set()
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = xy[i]
            x2, y2 = xy[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in xy_set and (x2, y1) in xy_set:
                rect = [xy[i], xy[j], (x1, y2), (x2, y1)]
                rect.sort()
                rect = tuple(rect)
                if rect not in counted:
                    ans += 1
                    counted.add(rect)
    
    
    print(ans)

if __name__ == '__main__':
    main()