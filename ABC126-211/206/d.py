import sys
from collections import defaultdict
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
    n = int(input())
    a = list(map(int, input().split()))

    out = set()
    for i in range(n//2 + n%2):
        if a[i] != a[n-1 - i]:
            out.add((a[i], a[n-1-i]))
    
    label_dict = dict()
    label = 0
    for a, b in out:
        if a not in label_dict.keys():
            label_dict[a] = label
            label += 1
        if b not in label_dict.keys():
            label_dict[b] = label
            label += 1
    
    m = label
    uf = UnionFind(m)
    for a, b in out:
        node1 = label_dict[a]
        node2 = label_dict[b]
        uf.union(node1, node2)

    ans = 0
    for group in uf.groups():
        ans += len(group) - 1 
    print(ans)


if __name__ == '__main__':
    main()