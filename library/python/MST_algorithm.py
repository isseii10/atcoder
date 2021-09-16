from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        """
        parents[x] := xが根の場合 -(xのグループの要素数)
                      それ以外の場合 親要素
        を返す
        つまりbySize
        """
        self.parents = [-1] * n

    def find(self, x):
        #findが呼ばれた時点で経路圧縮される(根へ繋ぎ換え)
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    #print用
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

    

# Kruskal法 UnionFind要る　O(|V|log|E|)
import heapq
def MST_Kruskal(n, edges):
    """
    n:頂点数
    edges:辺集合 (コスト, a, b) コストを[0]に置くことでコストの小さい順にheapqができる
    """
    uf = UnionFind(n)
    heapq.heapify(edges)
    MSTcost = 0
    while edges: #costの小さい順に取り出して、a,bが連結じゃなかったらつなげる
        edge_cost, a, b = heapq.heappop(edges)
        if not uf.is_same(a, b):
            uf.union(a, b)
            MSTcost += edge_cost
    
    return MSTcost


# Prim法
import heapq
def MST_Prim(n, G):
    """
    n:ノード数
    G:隣接リスト
    """

    #前処理(適当な頂点(ここでは0)から始めて、その頂点に繋がっている辺を全てhqにつっこむ)
    MST_cost = 0
    used = [False]*n #MSTとしてもうすでに使われたか？
    hq = [(c, w) for w, c in G[0]]
    used[0] = True
    heapq.heapify(hq)

    while hq:
        edge_cost, p = heapq.heappop(hq)
        if used[p]:
                continue
        MST_cost += edge_cost
        used[p] = 1
        for w, c in G[p]:
            if used[w]:
                continue
            heapq.heappush(hq, (c, w))

    return MST_cost