import sys
from collections import deque, defaultdict

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = 1<<60
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

    def is_same(self, x: int, y: int) -> bool:
        assert 0 <= x < self._n
        assert 0 <= y < self._n

        return self.find(x) == self.find(y)  # 根同じならTrue違うならFalseを返す

    def size(self, x: int) -> int:
        assert 0 <= x < self._n

        return -self.par_or_size[self.find(x)]
    
    def groups(self) -> typing.List[typing.List[int]]:
        find_buf = [self.find(i) for i in range(self._n)]

        group_list: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            group_list[find_buf[i]].append(i)
        return list(filter(lambda r: r, group_list))


def main():
    n, m = map(int, input().split())
    edges = [[] for _ in range(n)]
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        uf.union(a, b)
        edges[a].append(b)
        edges[b].append(a)
    
    #for i in range(n):
    #    if len(edges[i]) > 2:
    #        print(0)
    #        exit()

    def colored_count(group):
        #ひとつ目は３色にぬれる
        ret = 3
        p = group[0]
        colored = dict()
        for node in group:
            colored[node] = False
        colored[p] = True
        q = deque()
        q.append(p)
        while q:
            p = q.pop()
            for c in edges[p]:
                if colored[c]:continue
                color_c = 2
                for cc in edges[c]:
                    if cc == p:continue
                    if colored[cc]:
                        color_c -= 1
                color_c = max(0, color_c)
                ret *= color_c
                colored[c] = True
                q.append(c)
        
        return ret
    
    groups = defaultdict(list)
    for i in range(n):
        groups[uf.find(i)].append(i)

    ans = 1
    for group in groups.values():
        ans *= colored_count(group)
    print(ans)

    
    
if __name__ == '__main__':
    main()