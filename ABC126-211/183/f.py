import sys
from collections import defaultdict

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
    n, q = map(int, input().split())
    c = list(map(int, input().split()))
    num = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        class_name = c[i]
        num[i][class_name] += 1

    uf = UnionFind(n)

    for _ in range(q):
        q_type, x, y = map(int, input().split())
        x -= 1
        y -= 1
        if q_type == 1:
            if uf.is_same(x, y):continue
            #x, yをグループの根にする
            x = uf.find(x)
            y = uf.find(y)
            # -parents[a] でaのグループのサイズがわかるので、
            # (xのグループのサイズ) > (yのグループのサイズ)になるようにスワップ
            # サイズの大きいxのグループにサイズの小さいyのグループをマージ
            # (マージテク)
            if -uf.parents[x] < -uf.parents[y]:
                x, y = y, x
            for class_name, m in num[y].items():
                num[x][class_name] += m
            uf.union(x, y)
        else:
            print(num[uf.find(x)][y+1])
        #print(num)
        #print("==================================")




if __name__ == '__main__':
    main()