import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    r, c = map(int, input().split())
    s_y, s_x = map(int, input().split()) 
    g_y, g_x = map(int, input().split())
    s_y -= 1
    s_x -= 1
    g_x -= 1
    g_y -= 1

    def inside(y, x):
        return 0 <= y < r and 0 <= x < c

    maze = [input()[:-1] for _ in range(r)]
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dist = [[INF]*c for _ in range(r)]
    dist[s_y][s_x] = 0
    q = deque([(s_y, s_x)])
    while q:
        p_y, p_x = q.popleft()
        for dy, dx in move:
            c_y = p_y + dy
            c_x = p_x + dx
            if not inside(c_y, c_x):continue
            if maze[c_y][c_x] == "#":continue
            if dist[c_y][c_x] != INF:continue
            dist[c_y][c_x] = dist[p_y][p_x] + 1
            q.append((c_y, c_x))
    print(dist[g_y][g_x])

if __name__ == '__main__':
    main()