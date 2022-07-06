import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


class SegTree(object):
    def __init__(self, N, op, u_data):
        self._n = N
        self.log = (N-1).bit_length()
        self.size = 1 << self.log
 
        self.op = op
        self.e = u_data
 
        self.data = [u_data] * (2 * self.size)
        # self.len = [1] * (2 * self.size)
 
    def _update(self, i):
        self.data[i] = self.op(self.data[i << 1], self.data[i << 1 | 1])
 
    def initialize(self, arr=None):
        """ segtreeをarrで初期化する。len(arr) == Nにすること """
        if arr:
            for i, a in enumerate(arr, self.size):
                self.data[i] = a
        for i in reversed(range(1, self.size)):
            self._update(i)
            # self.len[i] = self.len[i << 1] + self.len[i << 1 | 1]
 
    def update(self, p, x):
        """ data[p] = x とする (0-indexed)"""
        p += self.size
        self.data[p] = x
        for i in range(1, self.log + 1):
            self._update(p >> i)
 
    def get(self, p):
        """ data[p]を返す """
        return self.data[p + self.size]
 
    def prod(self, l, r):
        """
        op(data[l], data[l+1], ..., data[r-1])を返す (0-indexed)
        """
        sml = self.e
        smr = self.e
        l += self.size
        r += self.size
 
        while l < r:
            if l & 1:
                sml = self.op(sml, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self.op(self.data[r], smr)
            l >>= 1
            r >>= 1
        return self.op(sml, smr)
 
    def all_prod(self):
        """ op(data[0], data[1], ... data[N-1])を返す """
        return self.data[1]
 
    def max_right(self, l, func):
        """
        func(l, l+1, ..., r-1) = True,
        func(l, l+1, ..., r-1, r) = Falseとなる r を返す
        """
        if l == self._n:
            return self._n
        l += self.size
        sm = self.e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not func(self.op(sm, self.data[l])):
                while l < self.size:
                    l <<= 1
                    if func(self.op(sm, self.data[l])):
                        sm = self.op(sm, self.data[l])
                        l += 1
                return l - self.size
            sm = self.op(sm, self.data[l])
            l += 1
            if (l & -l) == l:
                break
        return self._n
 
    def min_left(self, r, func):
        """
        func(     l, l+1, ..., r-1) = True,
        func(l-1, l, l+1, ..., r-1) = Falseとなる l を返す
        """
        if r == 0:
            return 0
        r += self.size
        sm = self.e
        while True:
            r -= 1
            while r > 1 and r & 1:
                r >>= 1
            if not func(self.op(self.data[r], sm)):
                while r < self.size:
                    r = r << 1 | 1
                    if func(self.op(self.data[r], sm)):
                        sm = self.op(self.data[r], sm)
                        r -= 1
                return r + 1 - self.size
            sm = self.op(self.data[r], sm)
            if (r & -r) == r:
                break
        return 0
 
 


def op(x:int, y:int) -> int:
    return x+y

def main():
    n = int(input())
    A = list(map(int, input().split()))
    st = SegTree(n+1, op, u_data=0)
    tentou = 0
    for a in A:
        tentou += st.prod(a+1, n)
        st.update(a, 1)
    
    for a in A:
        print(tentou)
        tentou += n-1-a - a
    
if __name__ == '__main__':
    main()