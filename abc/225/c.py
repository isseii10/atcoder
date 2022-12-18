import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]
    base = B[0][0]
    base_i = base // 7
    base_j = base % 7
    for i in range(n):
        for j in range(m):
            if B[i][j] == (base_i+i)*7 + (base_j+j):
                continue
            print("No")
            exit()
    print("Yes")
    

if __name__ == '__main__':
    main()