import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

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

        group_list: typing.List[typing.List[int]] = [[] for _ in range(self._n)]
        for i in range(self._n):
            group_list[find_buf[i]].append(i)
        return list(filter(lambda r: r, group_list))


def main():
    n, k, l = map(int, input().split())

    uf1 = UnionFind(n)
    for i in range(k):
        p, q = map(int, input().split())
        p -= 1
        q -= 1
        uf1.union(p,q)
    root1 = [uf1.find(i) for i in range(n)]

    uf2 = UnionFind(n)
    for j in range(l):
        r, s = map(int, input().split())
        r -= 1
        s -= 1
        uf2.union(r, s)
    root2 = [uf2.find(i) for i in range(n)]

    from collections import defaultdict
    d = defaultdict(int)
    for i in range(n):
        d[(root1[i], root2[i])] += 1 #根がスーパーノード(?)で、uf1でもuf2でも同じグループに属している頂点を数えている
    ans = []
    for i in range(n):
        ans.append(d[(root1[i], root2[i])])
    print(*ans)

if __name__ == '__main__':
    main()