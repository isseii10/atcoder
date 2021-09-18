import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    tx_a, ty_a, tx_b, ty_b, T, V = map(int, input().split())

    max_dist = T*V

    def check(x, y):
        dx1 = tx_a - x
        dy1 = ty_a - y
        dist1 = (dx1**2 + dy1**2)**0.5
        dx2 = tx_b - x
        dy2 = ty_b - y
        dist2 = (dx2**2 + dy2**2)**0.5
        return dist1 + dist2 <= max_dist


    n = int(input())
    girls = [tuple(map(int, input().split())) for _ in range(n)]
    for x, y in girls:
        if check(x, y):
            print("YES")
            break
    else:
        print("NO")

if __name__ == '__main__':
    main()