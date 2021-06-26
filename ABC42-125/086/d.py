import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353

def check_array(array):
    print("array is")
    for i in range(len(array)):
        print(array[i])

class Accumulate2(list):
    def __init__(self, array) -> None:
        self._array = array
        self.h = len(self._array)
        self.w = len(self._array[0])
        self.sum2d = [[0]*(self.w+1) for _ in range(self.h+1)]

    def build(self) -> None:
        for i in range(self.h):
            for j in range(self.w):
                self.sum2d[i+1][j+1] = (self.sum2d[i+1][j]
                                      + self.sum2d[i][j+1]
                                      - self.sum2d[i][j]
                                      + self._array[i][j])

    def get(self, a: tuple, b: tuple) -> int:
        """
        a, bは（y座標、x座標）なのに注意
        a:左上の点　b:右下の点
        bは含まない（半開）
        """
        ay, ax = a
        by, bx = b
        return self.sum2d[by][bx]-self.sum2d[by][ax]-self.sum2d[ay][bx]+self.sum2d[ay][ax]
        

def main():
    n, k = map(int, input().split())
    position_b = [[0]*(2*k) for _ in range((2*k))]
    for _ in range(n):
        x, y, c = input()[:-1].split()
        x = int(x)
        y = int(y)
        if c == 'W':
            y += k
        x %= 2*k
        y %= 2*k
        position_b[y][x] += 1
    #check_array(position_b)
    acc2d = Accumulate2(position_b)
    acc2d.build()
    #check_array(acc2d.sum2d)

    ans = 0
    for u in range(k+1):
        for l in range(k+1):
            r = l+k-1
            d = u+k-1
            # 左上(u,l),右上(u,r),左下(d,l),右下(d,r)
            #この４点はメインの四角の四角
            main_sq = acc2d.get((u, l), (d+1, r+1)) #メインの四角
            ul_sq = acc2d.get((0,0), (u,l)) #左上四角
            ur_sq = acc2d.get((0, r+1), (u, 2*k)) #右上四角
            dl_sq = acc2d.get((d+1, 0), (2*k, l)) # 左下四角
            dr_sq = acc2d.get((d+1, r+1), (2*k, 2*k)) #右下四角
            #print(u, l)
            #print(main_sq, ul_sq, ur_sq, dl_sq, dr_sq)
            res = main_sq + ul_sq + ur_sq + dl_sq + dr_sq
            ans = max(ans, res, n-res)
    print(ans)


            

        

if __name__ == '__main__':
    main()