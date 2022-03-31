from ast import iter_child_nodes
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n-1):
        if B[i][0] + 7 != B[i+1][0]:
            print("No")
            exit()
        for j in range(m-1):
            if B[i][j] + 1 != B[i][j+1]:
                print("No")
                exit()
    print("Yes")
if __name__ == '__main__':
    main()