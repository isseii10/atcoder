import sys

input = sys.stdin.readline
#sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

import typing
class UnionFind:
    def __init__(self, n) -> None:
        self._n = n
        self.par_or_size = [-1]*n
        

    def find(self, x: int) -> int:
        assert 0 <= x < self._n

        parent = self.par_or_size[x]
        while parent >= 0:
            if self.par_or_size[parent] < 0:
                return parent
            self.par_or_size[x], x, parent = (
                self.par_or_size[parent],
                self.par_or_size[parent],
                self.par_or_size[self.par_or_size[parent]]
            )
        return x

    def union(self, x: int, y: int) -> int:
        assert 0 <= x < self._n
        assert 0 <= y < self._n

        x = self.find(x)
        y = self.find(y)

        if x == y:
            return x

        if -self.par_or_size[x] < -self.par_or_size[y]:
                x, y = y, x
        
        self.par_or_size[x] += self.par_or_size[y]
        self.par_or_size[y] = x

        return x

    def same_check(self, x: int, y: int) -> bool:
        assert 0 <= x < self._n
        assert 0 <= y < self._n

        return self.find(x) == self.find(y)  # 根同じならTrue違うならFalseを返す

    def size(self, x: int) -> int:
        assert 0 <= x < self._n

        return -self.par_or_size[self.find(x)]
    
    def groups(self) -> typing.List[typing.List[int]]:
        find_buf = [self.find(i) for i in range(self._n)]

        group_list: typing.List[typing.List[int]] = [[] for _ in range(self.n)]
        for i in range(self.n):
            group_list[find_buf[i]].append(i)
        return list(filter(lambda r: r, group_list))


    
def main():
    import heapq
    n = int(input())
    xys_sortx = []
    xys_sorty = []
    for i in range(n):
        x, y = map(int ,input().split())
        xys_sortx.append((i, x, y))
        xys_sorty.append((i, x, y))
    
    xys_sortx.sort(key= lambda r:r[1])
    xys_sorty.sort(key= lambda r:r[2])
    edges = []
    for i in range(n-1):
        idx1, x1, y1 = xys_sortx[i]
        idx2, x2, y2 = xys_sortx[i+1]
        edges.append((min(abs(x2-x1), abs(y2-y1)), idx1, idx2))

        idx3, x3, y3 = xys_sorty[i]
        idx4, x4, y4 = xys_sorty[i+1]
        edges.append((min(abs(x4-x3), abs(y4-y3)), idx3, idx4))
    
    uf = UnionFind(n)
    heapq.heapify(edges)
    cost = 0
    while edges:
        c, a, b = heapq.heappop(edges)
        if not uf.same_check(a, b):
            uf.union(a, b)
            cost += c
    print(cost)


if __name__ == '__main__':
    main()