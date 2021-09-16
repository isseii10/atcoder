import sys
from heapq import heappop, heappush

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

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




def main():
    l, q = map(int, input().split())
    cx = [list(map(int, input().split())) for _ in range(q)]
    uf = UnionFind(l-1)
    cutting_points = set()
    for c, x in cx:
        if c == 1:
            cutting_points.add(x-1)
    
    for i in range(l-2):
        if i not in cutting_points and i+1 not in cutting_points:
            uf.union(i, i+1)
    #print(uf)

    ans_rev = []
    for c, x in cx[::-1]:
        if c == 1:
            #右端じゃなかったら
            if x != 1:
                uf.union(x-2, x-1)
            #左端じゃなかったら
            if x != l-1:
                uf.union(x-1, x)
        else:
            ans_rev.append(uf.size(x-1)+1)
        #print(uf)
    
    for a in ans_rev[::-1]:
        print(a)



    
if __name__ == '__main__':
    main()