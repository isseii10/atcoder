import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

INF = float('inf')
MOD = 10**9+7
#MOD = 998244353


def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    ans = 0
    for i in range(h):
        i += 1
        for j in range(w):
            j += 1
            if abs(i-r) + abs(j-c) == 1:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()