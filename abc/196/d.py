import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
MOD = 10**9+7
#MOD = 998244353



def main():
    H, W, A, B = map(int, input().split())
    
    used = [[False]*W for _ in range(H)]

    def dfs(h, w, a, b):
        res = 0
        if a < 0 or b < 0: return 0
        if w == W:
            w = 0
            h += 1
        if h == H: return 1

        if used[h][w]: return dfs(h, w+1, a, b)


        #bを使った遷移
        used[h][w] = True
        res += dfs(h, w+1, a, b-1)
        #aを横方向に使った遷移
        if w+1 < W and (not used[h][w+1]):
            used[h][w+1] = True
            res += dfs(h, w+1, a-1, b)
            used[h][w+1] = False
        #aを縦方向に使った遷移
        if h+1 < H and (not used[h+1][w]):
            used[h+1][w] = True
            res += dfs(h, w+1, a-1, b)
            used[h+1][w] = False
        
        used[h][w] = False
        return res
    
    print(dfs(0, 0, A, B))



        

            




if __name__ == '__main__':
    main()