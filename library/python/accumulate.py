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
        """
        ay, ax = a
        by, bx = b
        return self.sum2d[by][bx]-self.sum2d[by][ax]-self.sum2d[ay][bx]+self.sum2d[ay][ax]