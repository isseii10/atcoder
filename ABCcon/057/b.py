import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    n, m = map(int, input().split())
    students = [tuple(map(int, input().split())) for _ in range(n)]
    checks = [tuple(map(int, input().split())) for _ in range(m)]
    for a, b in students:
        dist = INF
        dist_idx = -1
        for j, (c, d) in enumerate(checks):
            if dist > abs(a-c) + abs(b-d):
                dist = abs(a-c) + abs(b-d)
                dist_idx = j+1
        print(dist_idx)

if __name__ == '__main__':
    main()