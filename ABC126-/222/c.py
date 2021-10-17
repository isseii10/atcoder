import sys
from functools import cmp_to_key

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    a = [list(input()[:-1]) for _ in range(2*n)]

    score_idx = [[0, i] for i in range(2*n)]

    win = [("P", "G"), ("C", "P"), ("G", "C")]
    lose = [("P", "C"), ("C", "G"), ("G", "P")]
    def win_x(a, b):
        if (a, b) in win:
            return 1
        elif (a, b) in lose:
            return 0
    
    def cmp(a, b):
        if a == b: return 0
        return -1 if a < b else 1
    
    def cmp_rev(a, b):
        if a == b:return 0
        return 1 if a < b else -1
    
    def cmptuple(a, b):
        return cmp(a[0], b[0]) or cmp_rev(a[1], b[1])
        
    #print(score_idx)
    for i in range(m):
        for j in range(n):
            score_x, idx_x = score_idx[2*j]
            score_y, idx_y = score_idx[2*j+1]
            te_x = a[idx_x][i]
            te_y = a[idx_y][i]
            if win_x(te_x, te_y) == 1:
                score_x += 1
            elif win_x(te_x, te_y) == 0:
                score_y += 1
            score_idx[2*j] = [score_x, idx_x]
            score_idx[2*j+1] = [score_y, idx_y]
        score_idx = sorted(score_idx, key=cmp_to_key(cmptuple))
        #print(score_idx)

    for _, idx in score_idx[::-1]:
        print(idx+1)
    
if __name__ == '__main__':
    main()