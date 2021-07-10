import sys
from math import pi, cos, sin

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353

def dot(A, B):
    # Aの列の次元とBの行の次元が違う時の動作は考えていない
    # A n行m列　n = len(A)
    # B m行l列 m = len(B)
    # C = A*B n行l列
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C 


def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x_op, y_op = map(int, input().split())

    x_c, y_c = (x0 + x_op)/2, (y0+y_op)/2
    theta = (2 * pi)/ n # rad

    A = [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]

    ans = dot(A, [[x0-x_c], [y0-y_c]])
    #print(ans)
    print(ans[0][0]+x_c, ans[1][0]+y_c)
    
if __name__ == '__main__':
    main()