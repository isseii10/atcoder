import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    a = [list(map(int, input().split())) for _ in range(4)]

    def is_inside(x, y):
        return 0 <= x < 4 and 0 <= y < 4
    
    move = [(1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)]
        
    def check_jouken(hei):
        x = -1
        y = -1
        for i in range(4):
            for j in range(4):
                if hei[i][j] == '#':
                    x = i
                    y = j
                    break
            else:
                continue
            break
        q = deque([(y, x)])
        visited = [[False]*4 for _ in range(4)]
        visited[y][x] = True
        while q:
            y, x = q.popleft()
            for dy, dx in move:
                ny = y + dy
                nx = x + dx
                if not is_inside(ny, nx):continue
                if hei[ny][nx] == ".":continue
                if visited[ny][nx]:continue
                visited[ny][nx] = True
                q.append((ny, nx))
        
        for i in range(4):
            for j in range(4):
                if not visited[i][j] and hei[i][j] == "#":
                    return False
        return True

    def check_hei_a(hei):
        for i in range(4):
            for j in range(4):
                if hei[i][j] == "." and a[i][j] == 1:
                    return False
        return True


    ans = 0
    counted_hei = set()
    for i in range(1 << 16):
        hei = [["."]*4 for _ in range(4)]
        for j in range(16):
            if i >> j & 1:
                y = j // 4
                x = j % 4
                hei[y][x] = "#"
        if not check_hei_a(hei):continue
        if check_jouken(hei):
            print("=================")
            for i in range(4):
                print(hei[i])
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()