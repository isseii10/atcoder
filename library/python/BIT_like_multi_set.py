# 要素の追加　O(log n)
# 要素の削除 O(log n)
# 要素のk番目を取得 O(log n)

class BinaryIndexTree:
    def __init__(self, n) -> None:
        self._n = n
        self.bit = [0]*(n+1) # 1-indexed
    
    def add(self, x, v):
        # bit[x]にvalueを追加
        while x <= self._n:
            self.bit[x] += v
            x += x & -x
    
    def sum(self, x):
        # bit[1]からbit[x]までの和
        ret = 0
        while x > 0:
            ret += self.bit[x]
            x -= x & -x
        return ret

bit = BinaryIndexTree(5)
for i in range(5):
    bit.add(i, i+1)

print(bit.bit)
for i in range(5):
    print(bit.sum(i))

