import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, a, b = map(int, input().split())
    a -= 1
    b -= 1
    p, q, r, s = map(int, input().split())
    p -= 1
    q -= 1
    r -= 1
    s -= 1
    
    table = [["."]*(s-r+1) for _ in range(q-p+1)]
    for y in range(q-p+1):
        real_y = y+p
        for x in range(s-r+1):
            real_x = x+r
            if real_x + real_y == a+b:
                table[y][x] = "#"
            if (n-1 - real_x) + real_y == (n-1 - b) + a:
                table[y][x] = "#"
    for i in range(q-p+1):
        print("".join(table[i]))

if __name__ == '__main__':
    main()