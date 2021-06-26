def main():
    h, w, n, m = map(int, input().split())
    grid = [[0]*w for _ in range(h)]

    for _ in range(n):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grid[a][b] = 1

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        grid[a][b] = -1

    # light:1, block:-1, lighted:2, dark:0

    #right
    for i in range(h):
        now_state = False
        for j in range(w):
            if grid[i][j] == 2:continue
            elif grid[i][j] == 1:
                now_state = True
            elif grid[i][j] == -1:
                now_state = False
            else:
                if now_state:
                    grid[i][j] = 2

    #left
    for i in range(h):
        now_state = False
        for j in range(w)[::-1]:
            if grid[i][j] == 2:continue

            if grid[i][j] == 1:
                now_state = True
            elif grid[i][j] == -1:
                now_state = False
            else:
                if now_state:
                    grid[i][j] = 2

    #up
    for j in range(w):
        now_state = False
        for i in range(h)[::-1]:
            if grid[i][j] == 2:continue

            if grid[i][j] == 1:
                now_state = True
            elif grid[i][j] == -1:
                now_state = False
            else:
                if now_state:
                    grid[i][j] = 2

    #down
    for j in range(w):
        now_state = False
        for i in range(h):
            if grid[i][j] == 2:continue

            if grid[i][j] == 1:
                now_state = True
            elif grid[i][j] == -1:
                now_state = False
            else:
                if now_state:
                    grid[i][j] = 2

    ans = n
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 or grid[i][j] == -1 or grid[i][j]==0:continue
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()