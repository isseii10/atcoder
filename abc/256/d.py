import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n = int(input())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr.sort()
    #print(lr)
    xy = []
    next_left = -1
    for left in range(n):
        if left < next_left:continue
        l1, r1 = lr[left]
        right = left
        while right < n and r1 >= lr[right][0]:
            r1 = max(r1, lr[right][1])
            right += 1
        xy.append((l1, r1))
        next_left = right
    
    for x, y in sorted(xy):
        print(x, y)


if __name__ == '__main__':
    main()