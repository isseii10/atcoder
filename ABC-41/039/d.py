import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    image = [list(input()) for _ in range(h)]
    before_image = [["."]*w for _ in range(h)]
    after_image = [["."]*w for _ in range(h)]

    mawari = [(-1, -1),
              (-1, 0),
              (-1, 1),
              (0, -1),
              (0, 1),
              (1, -1),
              (1, 0),
              (1, 1)]

    def is_inside(a, b):
        return 0 <= a < h and 0 <= b < w
    
    def is_same(s, t):
        for i in range(h):
            for j in range(w):
                if s[i][j] != t[i][j]:
                    return False
        return True

    for y in range(h):
        for x in range(w):
            if image[y][x] == '.':continue
            for dy, dx in mawari:
                ny = y + dy 
                nx = x + dx
                if not is_inside(ny, nx):continue
                if image[ny][nx] == '.':
                    break
            else:
                before_image[y][x] = '#'
                after_image[y][x] = '#'
    
    for y in range(h):
        for x in range(w):
            if before_image[y][x] == '#':
                for dy, dx in mawari:
                    ny = y + dy
                    nx = x + dx
                    if not is_inside(ny, nx):continue
                    if before_image[ny][nx] == '#':continue
                    after_image[ny][nx] = '#'
    #for i in range(h):
    #    print(before_image[i])
    #for i in range(h):
    #    print(after_image[i])
    if is_same(image, after_image):
        print('possible')
        for i in range(h):
            print("".join(before_image[i]))
    else:
        print('impossible')

    
            


if __name__ == '__main__':
    main()