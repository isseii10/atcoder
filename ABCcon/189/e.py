#from sys import setrecursionlimit
#setrecursionlimit(10**7)
from sys import stdin
input = stdin.readline
INF = float('inf')

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
    xy = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())
    op = [input()[:-1].split() for _ in range(m)]

    dot_list = [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]]
    
    for i in range(m):
        if int(op[i][0]) == 1:
            C = dot([[0, 1, 0], [-1, 0, 0], [0, 0, 1]], dot_list[-1])
            dot_list.append(C)
        if int(op[i][0]) == 2:
            C = dot([[0, -1, 0], [1, 0, 0], [0, 0, 1]], dot_list[-1])
            dot_list.append(C)
        if int(op[i][0]) == 3:
            C = dot([[-1, 0, 2*int(op[i][1])], [0, 1, 0], [0, 0, 1]], dot_list[-1])
            dot_list.append(C)
        if int(op[i][0]) == 4:
            C = dot([[1, 0, 0], [0, -1, 2*int(op[i][1])], [0, 0, 1]], dot_list[-1])
            dot_list.append(C)


    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        b -= 1
        x, y = xy[b]
        ans_x, ans_y, _ = dot(dot_list[a], [[x], [y], [1]])
        print(ans_x[0], ans_y[0])
    
if __name__ == '__main__':
    main()