import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, a, b = map(int, input().split())
    table = [["#"]*b*n for _ in range(a*n)]
    
    def print_table():
        for i in range(a*n):
            print("".join(table[i]))

    white_black = [[0]*n for _ in range(n)]
    for i in range(n):
        if i != 0:
            white_black[i][0] = 1-white_black[i-1][0]
        for j in range(1, n):
            white_black[i][j] = 1 - white_black[i][j-1]
    
    #for i in range(n):
    #    print(white_black[i])
    for i in range(n):
        for j in range(n):
            color = white_black[i][j]
            if color == 0:
                node = "."
            else:
                node = "#"
            for x in range(a):
                for y in range(b):
                    table[i*a+x][j*b+y]= node
                    
    print_table()
if __name__ == '__main__':
    main()