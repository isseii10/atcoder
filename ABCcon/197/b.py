import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w, x, y = map(int, input().split())
    x -= 1
    y -= 1
    s = [input()[:-1] for _ in range(h)]
    tate = 0
    yoko = 0
    for i in range(y, w):
        if s[x][i] == '.':
            yoko += 1
        else:
            break

    for i in range(y)[::-1]:
        if s[x][i] == '.':
            yoko += 1
        else:
            break

    for i in range(x, h):
        if s[i][y] == '.':
            tate += 1
        else:
            break

    for i in range(x)[::-1]:
        if s[i][y] == '.':
            tate += 1
        else:
            break
    #print(tate)
    #print(yoko)
    print(tate+yoko-1)

if __name__ == '__main__':
    main()