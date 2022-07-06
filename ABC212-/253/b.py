import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    ss = [input()[:-1] for _ in range(h)]
    #for i in range(h):
    #    print(ss[i])
    komas = []
    for y in range(h):
        for x in range(w):
            if ss[y][x] == "o":
                komas.append(tuple([y, x]))
    koma1 = komas[0]
    koma2 = komas[1]
    print(abs(koma2[0]-koma1[0])+abs(koma2[1]-koma1[1]))


if __name__ == '__main__':
    main()