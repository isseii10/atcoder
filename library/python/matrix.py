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