import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353




def main():
    n, m = map(int, input().split())
    p = [-1]*n
    def find(x):
        if p[x] < 0:
            return x
        p[x] = find(p[x])
        return p[x]
    
    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:return #すでに同じ集合の時
        if p[x] < p[y]:
            # xの方がサイズ大きい時はyの方が大きいようにする
            x, y = y, x
        p[y] += p[x]
        p[x] = y
    
    # 根の頂点を列挙
    def roots():
        res = []
        for x, v in enumerate(p):
            if v < 0:
                res.append(x)
        return res

    G = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        # 大きい頂点番号へ辺を貼る
        if a > b:
            a, b = b, a
        G[a].append(b)
    ans_rev = [0]
    group_count = 0
    for node in range(1, n)[::-1]:
        unite_count = 0
        for c in G[node]:
            if find(node) != find(c):
                unite(node, c)
                unite_count += 1

        group_count += 1 - unite_count
        ans_rev.append(group_count)
    print(*ans_rev[::-1])


    
if __name__ == '__main__':
    main()