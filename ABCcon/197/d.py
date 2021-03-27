import sys
import math

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

def rot(kaku):
    kaku = kaku * (2 * math.pi) / 360
    return [[math.cos(-kaku), -math.sin(-kaku)],
              [math.sin(-kaku), math.cos(-kaku)]]

def length(vec1, vec2):
    return math.sqrt((vec1[0]-vec2[0])**2 + (vec1[1]-vec2[1])**2)
     

def main():
    n = int(input())
    x_0, y_0 = map(int, input().split())
    x_op, y_op = map(int, input().split())
    len_op = length((x_0, y_0), (x_op, y_op))
    naikaku = 180*(n-2)/n
    naikaku /= 2
    print(naikaku)
    vec = [[(x_op-x_0)/len_op], [(y_op-y_0)/len_op]]
    rotate = rot(naikaku)
    print(rotate)
    vec1 = dot(rotate, vec)
    print(vec1)
    ans_x = (vec1[0][0] + x_0)*len_op*math.cos(naikaku)
    ans_y = (vec1[1][0]+ y_0)*len_op*math.cos(naikaku)
    print(ans_x, ans_y)


if __name__ == '__main__':
    main()