import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353



def main():
    q = int(input())
    n = pow(2, 20)
    a = [-1]*n
    parent = [-1]*(n+1)

    def find(x):
        if parent[x] < 0:
            return x
        # ここで経路圧縮（根までつなぎかえ）
        parent[x] = find(parent[x])
        return parent[x]
    
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:return
        if x > y:
            x, y = y, x
        parent[y] += parent[x] # サイズ取得のため、この問題ではいらない
        parent[x] = y

    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            h = x
            idx = find(h%n)
            if idx == n:
                idx = find(0)
            a[idx] = x
            unite(idx, idx+1)
        else:
            print(a[x%n])
            
        
if __name__ == '__main__':
    main()