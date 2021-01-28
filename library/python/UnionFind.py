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

        group_list: typing.List[typing.List[int]] = [[] for _ in range(self.n)]
        for i in range(self.n):
            group_list[find_buf[i]].append(i)
        return list(filter(lambda r: r, group_list))