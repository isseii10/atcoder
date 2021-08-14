import sys
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

class SegTree(object):
    def __init__(self, N, op, u_data):
        """
        N := node数
        op := モノイド同士の演算
        u_data := 単位源
        """
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

def op(x, y):
    return min(x, y)
e = INF


def main():
    n, q = map(int, input().split())
    # in_ out_は各幼稚園の園児のレートのhq
    in_ = [[] for _ in range(200005)]
    out_ = [[] for _ in range(200005)]
    now = [-1]*n
    rate = [-1]*n
    for i in range(n):
        a, b = map(int, input().split())
        b -= 1
        now[i] = b
        rate[i] = a
        heapq.heappush(in_[b], -a)
    
    st = SegTree(200005, op, e)
    for i in range(200001):
        if not in_[i]:continue
        st.update(i, -in_[i][0])
    
    for _ in range(q):
        c, new_en = map(int, input().split())
        c -= 1
        new_en -= 1
        prev_en = now[c]
        now[c] = new_en
        #入園処理
        heapq.heappush(in_[new_en], -rate[c])
        st.update(new_en, -in_[new_en][0])

        #退園処理
        heapq.heappush(out_[prev_en], -rate[c])
        while in_[prev_en] and out_[prev_en] and in_[prev_en][0] == out_[prev_en][0]:
            heapq.heappop(in_[prev_en])
            heapq.heappop(out_[prev_en])
        if in_[prev_en]:
            st.update(prev_en, -in_[prev_en][0])
        else:
            st.update(prev_en, e)

        print(st.all_prod())


if __name__ == '__main__':
    main()