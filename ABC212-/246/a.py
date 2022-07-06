import inspect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    nodes = [list(map(int, input().split())) for _ in range(3)]
    xs = set()
    ys = set()
    xs.add(nodes[0][0])
    xs.add(nodes[1][0])
    xs.add(nodes[2][0])
    ys.add(nodes[0][1])
    ys.add(nodes[1][1])
    ys.add(nodes[2][1])
    for x in xs:
        for y in ys:
            if [x, y] in nodes:
                continue
            print(x, y)
if __name__ == '__main__':
    main()